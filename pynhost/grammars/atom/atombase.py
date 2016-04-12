from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class AtomBaseGrammar(DumboBaseGrammar):
    _shortcuts = {
        'beginningConditionalSpace': '{ctrl+alt+1}',
        'endConditionalSpace': '{ctrl+alt+2}',
        'up': '{ctrl+alt+shift+up}',
        'right': '{ctrl+alt+shift+right}',
        'down': '{ctrl+alt+shift+down}',
        'left': '{ctrl+alt+shift+left}',
        'clearSelect': '{ctrl+alt+3}',
        'previousTab': '{ctrl+alt+4}',
        'nextTab': '{ctrl+alt+5}',

    }
    def __init__(self):
        super().__init__()

    def do_command(self, letters):
        api.send_string('{ctrl+alt+7}' + letters + '`')

    def goodbye(self, words):
        iter_count = int(words[-1])
        for i in range(iter_count):
            api.send_string('Goodbye World!')
