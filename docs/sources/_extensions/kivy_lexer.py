from kivy.extras.highlight import KivyLexer


def setup(app):
    app.add_lexer("kv", KivyLexer)
