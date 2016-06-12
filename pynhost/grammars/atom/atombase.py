from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class AtomBaseGrammar(DumboBaseGrammar):

    def __init__(self):
        self.app_context = 'Atom'
        super().__init__()

    def do_command(self, letters):
        api.send_string('{ctrl+alt+7}' + letters + '`')

    def goodbye(self, words):
        iter_count = int(words[-1])
        for i in range(iter_count):
            api.send_string('Goodbye World!')
