from pynhost.grammars.atom.atombase import AtomBaseGrammar
from pynhost import api
import time

class AtomDictationGrammar(AtomBaseGrammar):
    '''
    Barebones grammar class that can be used as a template for new
    grammars. See grammars/sample2.py for a more indepth example
    of grammars.
    '''
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
            'until': 't'
        }

        self.mapping = {
            '[{}] {} <num> <0->'.format(self.cmb(self._actions), self.cmb(self.numbered_directions)): self.numbered_action,
            '[{}] {} {} [<num>]'.format(self.cmb(self._actions), self.cmb(self.limits), self.cmb(self.all_chars)): self.scan,
            'sample goodbye <num>': self.goodbye
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

    def scan(self, words):
        count = str(self._num(words))
        action_letter = self._actions.get(words[0], '_m')[1]
        if words[0] in self._actions:
            words = words[1:]
        limit_letter = self.limits[words[0]]
        command = action_letter + limit_letter + self.all_chars[words[1]] + count
        print(command)
        self.do_command(command)
