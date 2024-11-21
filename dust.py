from antlr4 import *
from dust_grammar.DustGrammarLexer import DustGrammarLexer
from dust_grammar.DustGrammarParser import DustGrammarParser
from visitor import DustVisitor
from syntax_error_listener import DustErrorListener


def main() -> None:
    with open('input.ds') as file:
        prog = file.read()    

    lexer = DustGrammarLexer(InputStream(prog))       
    stream = CommonTokenStream(lexer)    
    parser = DustGrammarParser(stream)    
    parser.removeErrorListeners()
    syntax_error_listener = DustErrorListener()
    parser.addErrorListener(syntax_error_listener)            
    tree = parser.program()
    if syntax_error_listener.has_errors:
        print('Compilation finished with errors:')
        print('\n'.join(syntax_error_listener.errors))
        return

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
