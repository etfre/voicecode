from pynhost.grammars.atom.atombase import AtomBaseGrammar

class PythonKeywordsGrammar(AtomBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'Atom'
        self.dict_file = 'python.json'
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

    def goodbye(self, words):
        iter_count = int(words[-1])
        for i in range(iter_count):
            api.send_string('Goodbye World!')
