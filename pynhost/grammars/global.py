from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CommandPromptGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'global.json'
        self.mapping = {

        }
        self.load_numbered_command('enter')
        self.load_command('escape')
        self.load_numbered_command('snipe')
        self.load_numbered_command('tab')
        self.load_numbered_command('paste')

    def restart_server(self, words):
        api.send_string('{ctrl+c}')
        time.sleep(.2)
        api.send_string('python manage.py runserver{enter}')
