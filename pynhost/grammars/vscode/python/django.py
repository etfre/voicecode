from pynhost.grammars.atom.atombase import AtomBaseGrammar

class DjangoGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.dict_file = 'django.json'
        self.context_filters = {
            'language': 'python'
        }
        self.load_all_commands()
