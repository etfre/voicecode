from pynhost import grammarbase, api
from pynhost.grammars.dumbobase import DumboBaseGrammar

class VSCodeBaseGrammar(DumboBaseGrammar):

    _shortcuts = {
        'begSpace': '{ctrl+alt+shift+b}',
        'endSpace': '{ctrl+alt+shift+v}',
        'up': '{ctrl+alt+shift+up}',
        'right': '{ctrl+alt+shift+right}',
        'down': '{ctrl+alt+shift+down}',
        'left': '{ctrl+alt+shift+left}',
        'clearSelect': '{ctrl+alt+3}',
        'previousTab': '{ctrl+alt+4}',
        'nextTab': '{ctrl+alt+5}',
        'setMark': '{ctrl+alt+shift+l}',
        'selectFromMark': '{ctrl+alt+shift+z}',

    }

    def __init__(self):
        self.app_context = 'Visual'
        super().__init__()

    def do_command(self, letters):
        api.send_string('{ctrl+alt+7}' + letters + '`')

    def goodbye(self, words):
        iter_count = int(words[-1])
        for i in range(iter_count):
            api.send_string('Goodbye World!')
