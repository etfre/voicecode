from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class AtomCommandsGrammar(DumboBaseGrammar):
    def __init__(self):
        super().__init__()
        self.dict_file = 'atomcmds.json'
        self.mapping = {
        }
        self.load_command('join lines')
        self.load_command('toggle comment')
        self.load_numbered_command('undo')
        self.load_numbered_command('snipe') # backspace


    def letter(self, words):
        api.send_string(words[0][0])

    def char(self, words):
        api.send_string(self._other_chars[words[0]])
