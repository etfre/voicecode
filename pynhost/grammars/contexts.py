from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class ContextsGrammar(DumboBaseGrammar):
    def __init__(self):
        super().__init__()
        self.mapping = {
            'enable <any> <1->': self.change_context,
            'activate <any> <1->': self.open_window
        }
    def change_context(self, words):
        self.change_global_context(words[1], ' '.join(words[2:]))

    def open_window(self, words):
        api.activate_window(words[-1])
