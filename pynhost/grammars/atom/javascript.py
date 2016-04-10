from pynhost.grammars.atom.atombase import AtomBaseGrammar

class JavascriptKeywordsGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.context_filters = {
            'language': 'javascript'
        }
        self.dict_file = 'javascript.json'
        self.load_command('new function')
    
