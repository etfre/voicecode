from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CharactersGrammar(DumboBaseGrammar):
    def __init__(self):
        super().__init__()
        self.mapping = {
            '[shrink] ({})'.format('|'.join(self._operators)): self.operator,
        #     '({})'.format('|'.join(self._other_chars)): self.char,
        }
        self.dict_file = 'chars.json'
        self.load_all_numbered_commands()
        self.mapping.pop('plus <num> <0->', None)
        self.mapping.pop('dash <num> <0->', None)
        self.mapping.pop('greater <num> <0->', None)
        self.mapping.pop('lesser <num> <0->', None)
        self.mapping.pop('star <num> <0->', None)
        self.mapping.pop('ekebefore <num> <0->', None)
        self.mapping.pop('compare <num> <0->', None)

    def letter(self, words):
        api.send_string(words[0][0])

    def char(self, words):
        api.send_string(self._other_chars[words[0]])

    def operator(self, words):
        if words[0] == 'shrink':
            text = self._operators[words[1]]
        else:
            text = self.space(self._operators[words[0]])
        api.send_string(text, delay=.1)
