from pynhost.grammars.vscode.vscodebase import VSCodeBaseGrammar
from pynhost import api

class VSCodeDictationGrammar(VSCodeBaseGrammar):
    '''
    Barebones grammar class that can be used as a template for new
    grammars. See grammars/sample2.py for a more indepth example
    of grammars.
    '''
    def __init__(self):
        super().__init__()
        self.mapping = {
            '(camel|score|word|dictate|title) <any><1->': self.dictate,
        }

    def dictate(self, words):
        if words[0] == 'camel':
            api.send_string(words[1] + ''.join(w.title() for w in words[2:]))
        elif words[0] == 'score':
            api.send_string('_'.join(words[1:]))
        elif words[0] == 'word':
            api.send_string(''.join(words[1:]))
        elif words[0] == 'dictate':
            api.send_string(' '.join(words[1:]))
        elif words[0] == 'title':
            api.send_string(''.join(w.title() for w in words[1:]))
