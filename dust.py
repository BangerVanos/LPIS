from antlr4 import *
from dust_grammar.DustGrammarLexer import DustGrammarLexer
from dust_grammar.DustGrammarParser import DustGrammarParser
from dust_grammar.DustGrammarVisitor import DustGrammarVisitor


class DustVisitor(DustGrammarVisitor):

    def __init__(self) -> None:
        super(DustVisitor, self).__init__()
    
    def visitProgram(self, ctx: DustGrammarParser.ProgramContext):
        print('Meh...')
        return super().visitProgram(ctx)

def main() -> None:
    with open('input.ds') as file:
        prog = file.read()
    print(f'PROG TEXT:\n{prog}')

    lexer = DustGrammarLexer(InputStream(prog))    
    stream = CommonTokenStream(lexer)
    parser = DustGrammarParser(stream)
    tree = parser.program()
    visitor = DustVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
