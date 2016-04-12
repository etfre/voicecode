from pynhost.grammars.atom.atombase import AtomBaseGrammar

class TreeViewGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.mapping = {
        }
        self.dict_file = 'treeview.json'
        self.load_command('tree focus')
        self.load_numbered_command('tree up')
        self.load_numbered_command('tree right')
        self.load_numbered_command('tree down')
        self.load_numbered_command('tree left')
        self.load_command('tree file')
        self.load_command('tree folder')
        self.load_command('tree duplicate')
        self.load_command('tree move')
        self.load_command('tree delete')
