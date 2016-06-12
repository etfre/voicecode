from pynhost.grammars.vscode.vscodebase import VSCodeBaseGrammar

class PythonKeywordsGrammar(VSCodeBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'python.json'
        self.context_filters = {
            'language': 'python'
        }
        self.mapping = {
            # 'new set': self.command['new set'],
            # 'new class': self.command['new class'],
            # 'new function': self.command['new function'],
            # 'condition': self.space(self.command['condition'], start=False), #if
            # 'while': 'while' + self._shortcuts['endConditionalSpace'],
            # 'yield': 'yield' + self._shortcuts['endConditionalSpace'],
            # 'continue': 'continue',
            # 'break': 'break',
        }
        self.load_all_commands()

    def load_literal(self, text):
        self.load_command('crunk {}'.format(text))

class PythonSpacesGrammar(VSCodeBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'python/spaced.json'
        self.context_filters = {
            'language': 'python'
        }
        self.load_all_commands()
        self.load_all_numbered_commands()
        self.mapping = {
            'import': self._shortcuts['begSpace'] + 'import' + self._shortcuts['endSpace'],
            'from': self._shortcuts['begSpace'] + 'from' + self._shortcuts['endSpace'],
        }
        

    def load_literal(self, text):
        self.load_command('crunk {}'.format(text))