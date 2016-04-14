from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CommandPromptGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'global.json'
        self.mapping = {
            'num <num> <1->': self.number
        }
        self.load_numbered_command('enter')
        self.load_command('escape')
        self.load_numbered_command('snipe')
        self.load_numbered_command('bell') #delete
        self.load_numbered_command('tab')
        self.load_numbered_command('paste')

    def number(self, words):
        num = str(self._num(words))
        api.send_string(num)
