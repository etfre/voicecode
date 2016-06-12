from pynhost import api
import time
from pynhost.grammars.dumbobase import DumboBaseGrammar

class CommandPromptGrammar(DumboBaseGrammar):

    def __init__(self):
        super().__init__()
        self.dict_file = 'cmdprompt.json'
        self.app_context = 'command'
        self.load_all_commands()
        self.mapping['django restart server'] = self.restart_server
        self.mapping['climb [<num>]'] = self.go_up_directory

    def restart_server(self, words):
        api.send_string('{ctrl+c}')
        time.sleep(.2)
        api.send_string('python manage.py runserver{enter}')

    def go_up_directory(self, words):
        num = self._num(words)
        text = 'cd ' + '/'.join(['..' for n in range(num)]) + '{enter}'
        api.send_string(text)
