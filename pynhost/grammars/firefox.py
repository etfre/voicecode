from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class FirefoxGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.app_context = 'mozilla firefox'
        self.dict_file = 'firefox.json'
        self.load_all_commands()
