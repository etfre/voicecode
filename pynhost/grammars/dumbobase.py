from pynhost import grammarbase, api
import json
import os

class DumboBaseGrammar(grammarbase.GrammarBase):

    dictionary_root = os.path.join('..', 'dictionary')
    dict_file = None

    _shortcuts = {
        'beginningConditionalSpace': '{ctrl+alt+1}',
        'endConditionalSpace': '{ctrl+alt+2}',
        'begSpace': '{ctrl+alt+shift+b}',
        'endSpace': '{ctrl+alt+shift+v}',
        'up': '{ctrl+alt+shift+up}',
        'right': '{ctrl+alt+shift+right}',
        'down': '{ctrl+alt+shift+down}',
        'left': '{ctrl+alt+shift+left}',
        'clearSelect': '{ctrl+alt+3}',
        'previousTab': '{ctrl+alt+4}',
        'nextTab': '{ctrl+alt+5}',
    }

    _operators = {
        'compare': '==',
        'star': '*',
        'dash': '-',
        'greater': '>',
        'lesser': '<',
        'plus': '+',
        'eke': '=',
        "percent": '%',
    }

    _letters = {
        'alpha': 'a',
        'bravo': 'b',
        'charlie': 'c',
        'delta': 'd',
        'echo': 'e',
        'foxtrot': 'f',
        'golf': 'g',
        'india': 'i',
        'hotel': 'h',
        'juliet': 'j',
        'kilo': 'k',
        'lima': 'l',
        'mike': 'm',
        'november': 'n',
        'oscar': 'o',
        'papa': 'p',
        'quebec': 'q',
        'romeo': 'r',
        'sierra': 's',
        'tango': 't',
        'uniform': 'u',
        'victor': 'v',
        'whiskey': 'w',
        'x-ray': 'x',
        'yankee': 'y',
        'zulu': 'z',
    }

    _other_chars = {
        "frog": "(",
        "toad": ")",
        "lace": "{{",
        "race": "}}",
        "lack": "[",
        "rack": "]",
        "dash": "-",
        "eke": "=",
        "plus": "+",
        "bar": "-",
        "star": "*",
        "lesser": "<",
        "greater": ">",
        "semicolon": ";",
        "colon": ":",
        "wave": "",
        "comma": ",",
        "beer": ".",
        "space": " ",
        "percent": "%",
        "single": "'",
        "double": "\""
    }

    all_chars = _letters.copy()
    all_chars.update(_other_chars)

    def __init__(self):
        super().__init__()

    @property
    def dict_file(self):
        return ''

    @dict_file.setter
    def dict_file(self, value):
        self.dict_obj = self.dict_json(os.path.join(self.dictionary_root, value))

    @property
    def command(self):
        return self.dict_obj.get('Commands', {})

    @property
    def num_command(self):
        return self.dict_obj.get('NumberedCommands', {})

    def cmb(self, container):
        return '({})'.format('|'.join(container))

    def dict_json(self, path):
        with open(path) as f:
            return json.loads(f.read())

    def _num(self, arr, default=1):
        num_str = ''
        while arr and arr[-1].isdigit():
            num_str = arr.pop() + num_str
        return int(num_str) if num_str else default

    def space(self, text, start=True, end=True):
        start = self._shortcuts['begSpace'] if start else ''
        end = self._shortcuts['endSpace'] if end else ''
        return '{}{}{}'.format(start, text, end)

    def load_command(self, text):
        self.mapping[text] = self.command[text]

    def load_numbered_command(self, text):
        rule = '{} <num> <0->'.format(text)
        self.mapping[rule] = self.num_cmd_func

    def load_all_commands(self):
        for cmd, text in self.command.items():
            if text:
                self.load_command(cmd)

    def load_all_numbered_commands(self):
        for cmd, text in self.num_command.items():
            if text:
                self.load_numbered_command(cmd)

    def num_cmd_func(self, words):
        count = self._num(words)
        text = self.num_command[' '.join(words)]
        for i in range(count):
            api.send_string(text)
