from antlr4.error.ErrorListener import *


class DustErrorListener(ErrorListener):
    has_errors = False

    def __init__(self) -> None:
        super().__init__()
        self._syntax_errors: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, type_error):
        red_error = "\033[31;1mSyntax error\033[0m:"

        def replace_eof(replace_str: str):
            return replace_str.replace("<EOF>", "empty")

        msg = replace_eof(msg)
        self.has_errors = True
        self._syntax_errors.append(f"{red_error} Line {line} Column {column}: {msg}")
    
    @property
    def errors(self) -> list[str]:
        return self._syntax_errors
