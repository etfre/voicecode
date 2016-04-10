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
        }

        self.mapping = {
            '[{}] {} <num> <0->'.format(self.cmb(self._actions), self.cmb(self.numbered_directions)): self.numbered_action,
            '[{}] {} {} <1-> [<num>]'.format(self.cmb(self._actions), self.cmb(self.limits), self.cmb(self.all_chars)): self.scan,
            '{} {} [<num>]'.format(self.cmb(self._actions), self.cmb(self.text_objects)): self.manip_text_object,
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
        for i in range(num):
            api.send_string(text_obj + action)

    def scan(self, words):
        count = str(self._num(words))
        action_letter = self._actions.get(words[0], '_m')[1]
        if words[0] in self._actions:
            words = words[1:]
        limit_letter = self.limits[words[0]]
        search_text = ''.join(self.all_chars[word] for word in words[1:])
        command = action_letter + limit_letter + search_text + count
        self.do_command(command)
