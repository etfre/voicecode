from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class ContextsGrammar(DumboBaseGrammar):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'enable <any> <1->': self.change_context,
            'activate <any> <1->': self.open_window,
            'maximize': self.maximize_window,
        }
    def change_context(self, words):
        self.change_global_context(words[1], ' '.join(words[2:]))

    def open_window(self, words):
        aliases = {
            'code': 'visual studio code',
            'chrome': 'google chrome',
        }
        window_name = ' '.join(words[1:])
        if window_name in aliases:
            window_name = aliases[window_name]
        api.activate_window(window_name)
        
    def maximize_window(self, words):
        api.maximize_active_window()
