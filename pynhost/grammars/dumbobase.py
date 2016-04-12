from pynhost import grammarbase, api
import json
import os

class DumboBaseGrammar(grammarbase.GrammarBase):

    dictionary_root = os.path.join('..', 'dictionary')
    dict_file = None
    print(os.getcwd())

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
        start = self._shortcuts['beginningConditionalSpace'] if start else ''
        end = self._shortcuts['endConditionalSpace'] if end else ''
        return '{}{}{}'.format(start, text, end)

    def load_command(self, text):
        self.mapping[text] = self.command[text]

    def load_numbered_command(self, text):
        rule = '{} <num> <0->'.format(text)
        self.mapping[rule] = self.num_cmd_func

    def num_cmd_func(self, words):
        count = self._num(words)
        text = self.num_command[' '.join(words)]
        for i in range(count):
            api.send_string(text)
