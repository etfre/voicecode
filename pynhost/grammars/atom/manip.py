from pynhost.grammars.atom.atombase import AtomBaseGrammar
from pynhost import api
import time

class AtomDictationGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'

        self._actions = {
            'delete': ('{delete}', 'k'),
            'copy': ('{ctrl+c}', 'y'),
            'grab': ('{ctrl+x}', 'd'),
            'select': ('', 's'),
        }
        self.numbered_directions = {
            'up': '{up}',
            'right': '{right}',
            'down': '{down}',
            'left': '{left}',
        }
        self.limits = {
            'until': 't',
            'after': 'f',
            'before': 'F',
        }

        self.text_objects = {
            'word': '{ctrl+d}',
            'line': '{ctrl+l}',
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
            '[{}] {} {} <1-> [<num>]'.format(self.cmb(self._actions), self.cmb(self.limits), self.cmb(self.all_chars)): self.scan,
            '{} {} [<num>]'.format(self.cmb(self._actions), self.cmb(self.text_objects)): self.manip_text_object,
            '[{}] (west|east)'.format(self.cmb(self._actions), self.cmb(self.text_objects)): self.manip_text_object_card,
            '[{}] (inside|outside) {}'.format(self.cmb(self._actions), self.cmb(self.surround_limits)): self.surround_action,
        }

    def numbered_action(self, words):
        action = self._actions.get(words[0], [None])[0]
        count = self._num(words)
        if action is None:
            send_str = ''.join([self._shortcuts[words[0]] for i in range(count)])
        else:
            keys = '+'.join([self.numbered_directions[words[1]][1:-1] for i in range(count)])
            send_str = '{shift+' + keys + '}' + action
        api.send_string(send_str)

    def manip_text_object(self, words):
        num = self._num(words)
        text_obj = self.text_objects[' '.join(words[1:])]
        action = self._actions[words[0]][0]
        cleanup = '' if words[0] != 'copy' else self._shortcuts['clearSelect']
        command = (text_obj + action + cleanup) * num
        api.send_string(command)

    def manip_text_object_card(self, words):
        action = self._actions.get(words[0], '')
        if action:
            action = action[0]
        cleanup = '' if words[0] != 'copy' else self._shortcuts['clearSelect']
        text_obj = self.text_objects[words[-1]]
        if len(words) > 1:
            print('{{shift+{}}}{}{}'.format(text_obj, action, cleanup))
            api.send_string('{{shift+{}}}{}{}'.format(text_obj, action, cleanup))
        else:
            api.send_string('{{{}}}{}{}'.format(text_obj, action, cleanup))

    def surround_action(self, words):
        action_letter = self._actions.get(words[0], '_s')[1]
        command = '{}s{}{}1'.format(action_letter, self.surround_limits[words[-1]], words[-2][0])
        print(command)
        self.do_command(command)

    def scan(self, words):
        count = str(self._num(words))
        action_letter = self._actions.get(words[0], '_m')[1]
        if words[0] in self._actions:
            words = words[1:]
        limit_letter = self.limits[words[0]]
        search_text = ''.join(self.all_chars[word] for word in words[1:])
        command = action_letter + limit_letter + search_text + count
        self.do_command(command)
