from pynhost.grammars.atom.atombase import AtomBaseGrammar

class TreeViewGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.mapping = {
        }
        self.dict_file = 'treeview.json'
        self.load_all_numbered_commands()
        self.load_all_commands()
