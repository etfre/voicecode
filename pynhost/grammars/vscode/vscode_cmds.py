from pynhost import grammarbase, api
from pynhost.grammars.vscode.vscodebase import VSCodeBaseGrammar

class VSCodeCommandsGrammar(VSCodeBaseGrammar):
    def __init__(self):
        super().__init__()
        self.dict_file = 'vscodecmds.json'
        self.mapping = {
            'spark <num> <1->': self.go_to_line,
            'halt': self.space(',', start=False),
            'new scope': self.space('{{}}{left}{enter}{tab}', end=False)

        }
        self.load_all_commands()
        self.load_all_numbered_commands()
        # self.load_numbered_command('undo'),
        # self.load_numbered_command('duplicate line'),
        # self.load_numbered_command('flip down'),
        # self.load_numbered_command('flip up'),
        # self.load_numbered_command('buffer left'),
        # self.load_numbered_command('buffer right'),
        # self.load_numbered_command('snipe') # backspace
        # self.load_numbered_command('indent') # backspace
        # self.load_numbered_command('outdent') # backspace


    def go_to_line(self, words):
        num = self._num(words)
        api.send_string('{ctrl+g}' + str(num) + '{enter}')

    def letter(self, words):
        api.send_string(words[0][0])

    def char(self, words):
        api.send_string(self._other_chars[words[0]])
