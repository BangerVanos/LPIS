from antlr4 import *
from dust_grammar.DustGrammarLexer import DustGrammarLexer
from dust_grammar.DustGrammarParser import DustGrammarParser
from visitor import DustVisitor


def main() -> None:
    with open('input.ds') as file:
        prog = file.read()
    # print(f'PROG TEXT:\n{prog}')

    lexer = DustGrammarLexer(InputStream(prog))    
    stream = CommonTokenStream(lexer)
    parser = DustGrammarParser(stream)
    tree = parser.program()    
    visitor = DustVisitor()    
    visitor.visit(tree)
    if len(visitor.errors) == 0:
        with open('dust_compiled.py', 'w') as file:
            file.write(visitor.code)
        print('Compilation finished successfully')
    else:
        print('Compilation finished with errors:')
        print('\n'.join(visitor.errors))
        

if __name__ == '__main__':
    main()
