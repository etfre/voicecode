from pynhost.grammars.vscode.vscodebase import VSCodeBaseGrammar
from pynhost import api
import time

class AtomDictationGrammar(VSCodeBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'chars.json'
        self._actions = {
            'delete': '{delete}',
            'copy': '{ctrl+c}',
            'grab': '{ctrl+x}',
            'select': '',
        }
        self.numbered_directions = {
            'up': '{ctrl+alt+shift+w}',
            'right': '{ctrl+alt+shift+d}',
            'down': '{ctrl+alt+shift+s}',
            'left': '{ctrl+alt+shift+a}',
        }
        self.limits = {
            'until': '{left}',
            'after': '{right}',
            'before': '{left}',
        }

        self.text_objects = {
            'word': '{ctrl+d}',
            'spark': '{ctrl+i}',
            'module': '{ctrl+a}',
            'east': 'end',
            'west': 'home'
        }

        self.surround_limits = {
            'par': '()',
            'braces': '{}',
            'brackets': '[]',
            'chevrons': '<>',
            'single': "''",
            'double': '""',
        }

        self.mapping = {
            '[{}] {} <num> <0->'.format(self.cmb(self._actions), self.cmb(self.numbered_directions)): self.numbered_action,
            '[{}] {} [grow] {} <1-> [<num>]'.format(self.cmb(self._actions), self.cmb(self.limits), self.cmb(self.num_command)): self.scan,
            '{} {} <num> <0->'.format(self.cmb(self._actions), self.cmb(self.text_objects)): self.manip_text_object,
            '[{}] (west|east)'.format(self.cmb(self._actions), self.cmb(self.text_objects)): self.manip_text_object_card,
            '[{}] (inside|outside) {}'.format(self.cmb(self._actions), self.cmb(self.surround_limits)): self.surround_action,
        }

    def numbered_action(self, words):
        action = self._actions.get(words[0], None)
        count = self._num(words)
        if action is None:
            send_str = ('{' + words[0] + '}') * count
            # send_str = ''.join([self._shortcuts[words[0]] for i in range(count)])
        else:
            # send_str = '{shift}' + (('{' + words[0] + '}') * count) + action
            send_str = ''.join(['{shift+' + words[1] + '}' + action for i in range(count)])
        api.send_string(send_str)

    def manip_text_object(self, words):
        num = self._num(words)
        text_obj = self.text_objects[' '.join(words[1:])]
        action = self._actions[words[0]]
        cleanup = '' if words[0] != 'copy' else '{esc}'
        if text_obj == '{ctrl+i}' and words[0] in ('grab', 'delete'):
            cleanup += '{back}'
        command = (text_obj * num) + action + cleanup
        print(command)
        api.send_string(command)

    def manip_text_object_card(self, words):
        action = self._actions.get(words[0], '')
        if action:
            action = action[0]
        cleanup = '' if words[0] != 'copy' else self._shortcuts['clearSelect']
        text_obj = self.text_objects[words[-1]]
        if len(words) > 1:
            api.send_string('{{shift+{}}}{}{}'.format(text_obj, action, cleanup))
        else:
            api.send_string('{{{}}}{}{}'.format(text_obj, action, cleanup))

    def surround_action(self, words):
        action_letter = self._actions.get(words[0], '_s')[1]
        command = '{}s{}{}1'.format(action_letter, self.surround_limits[words[-1]], words[-2][0])
        self.do_command(command)

    def scan(self, words):
        count = self._num(words)
        action = self._actions.get(words[0], '')
        command = ''
        if words[0] in self._actions:
            command += self._shortcuts['setMark']
            words = words[1:]
        limit = self.limits[words[0]]
        if words[1] == 'grow':
            search_text = ''.join(self.num_command[word].title() for word in words[2:])
        else:
            search_text = ''.join(self.num_command[word] for word in words[1:])
        direction = '{f3}' * (count - 1)
        if words[0] in ('before',):
            direction = '{shift+f3}' * count
        command += '{ctrl+f}' + search_text + direction + '{esc}' + limit
        api.send_string(command)
        if command.startswith(self._shortcuts['setMark']):
            api.send_string(self._shortcuts['selectFromMark'])
            time.sleep(.1)
            api.send_string(action)
        # command = action_letter + limit_letter + search_text + count
        # self.do_command(command)
#
class VSCodeLowPriorityCUAGrammar(VSCodeBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = ''
        self.priority = -1
        self.mapping = {
            'grab': '{ctrl+x}',
            'copy': '{ctrl+x}{ctrl+v}',
            'paste': '{ctrl+v}',
        }
