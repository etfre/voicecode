from pynhost.grammars.atom.atombase import AtomBaseGrammar
from pynhost import api

class AtomDictationGrammar(AtomBaseGrammar):
    '''
    Barebones grammar class that can be used as a template for new
    grammars. See grammars/sample2.py for a more indepth example
    of grammars.
    '''
    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.mapping = {
            '(camel|score) <any><1->': self.dictate,
            'sample goodbye <num>': self.goodbye,
        }

    def dictate(self, words):
        print(words)
        if words[0] == 'camel':
            api.send_string(words[1] + ''.join([w.title() for w in words[2:]]))
        elif words[0] == 'score':
            api.send_string('_'.join(words[1:]))
