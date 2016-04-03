from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CharactersGrammar(DumboBaseGrammar):
    def __init__(self):
        super().__init__()
        # self.dict_file = 'chars.json'
        self.mapping = {
            '({})'.format('|'.join(self._letters)): self.letter,
            '({})'.format('|'.join(self._other_chars)): self.char,
        }

    def letter(self, words):
        api.send_string(words[0][0])

    def char(self, words):
        api.send_string(self._other_chars[words[0]])
