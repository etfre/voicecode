from pynhost.grammars.vscode.vscodebase import VSCodeBaseGrammar

class JavascriptKeywordsGrammar(VSCodeBaseGrammar):

    def __init__(self):
        super().__init__()
        self.context_filters = {
            'language': 'javascript'
        }
        self.dict_file = 'react.json'
        self.load_all_commands()
