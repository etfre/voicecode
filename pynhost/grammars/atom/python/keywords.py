from pynhost.grammars.atom.atombase import AtomBaseGrammar

class PythonKeywordsGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.dict_file = 'python.json'
        self.context_filters = {
            'language': 'python'
        }
        self.mapping = {
            'new set': self.command['new set'],
            'new class': self.command['new class'],
            'new function': self.command['new function'],
            'condition': self.space(self.command['condition'], start=False), #if
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'yield': 'yield' + self._shortcuts['endConditionalSpace'],
            'continue': 'continue',
            'break': 'break',
            'assert': 'assert' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],
            'while': 'while' + self._shortcuts['endConditionalSpace'],

            'sample goodbye <num>': self.goodbye,
        }
        self.load_literal('path')
        self.load_literal('os')
        self.load_literal('time')
        self.load_literal('dunder')


    def load_literal(self, text):
        self.load_command('crunk {}'.format(text))

    def goodbye(self, words):
        iter_count = int(words[-1])
        for i in range(iter_count):
            api.send_string('Goodbye World!')
