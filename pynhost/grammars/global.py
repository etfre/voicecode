from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CommandPromptGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'global.json'
        self.mapping = {
            'num <num> <1->': self.number,
            "click": self.click,
        }
        self.load_command('escape')
        self.load_all_numbered_commands()

    def number(self, words):
        num = str(self._num(words))
        api.send_string(num)

    def click(self, words):
        api.mouse_click()
