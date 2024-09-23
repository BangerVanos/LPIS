grammar DustGrammar;

//Parser

program : fn_decl* main_fn EOF;

// Basis
type : INT | BOOL | SET;
literal : NUMBER | TRUE | FALSE;
set : LBRACKET (expr (COMMA expr)*)? RBRACKET;
atom : ID | literal;
range : expr RANGE expr;
main_fn : FN 'main' LPAREN RPAREN BEGIN stmt* END;

expr
    : atom
    | set        
    | fn_call
    | unary_math expr
    | expr binary_math expr
    | unary_logical expr
    | expr binary_logical expr   
    | LPAREN expr RPAREN
    ;    

stmt
    : expr SEMICOLON
    | assign SEMICOLON
    | var_decl SEMICOLON
    | return SEMICOLON    
    | if_stmt
    | for_stmt
    | while_stmt
    | print_fn
    | println_fn
    | SEMICOLON;

//Operations
assign : ID (COMMA ID)* ASSIGN expr (COMMA expr)*;
unary_logical : NEGATION;
binary_logical
    : EQUAL 
    | NON_EQUAL 
    | LESS 
    | GREATER 
    | LESS_OR_EQUAL 
    | GREATER_OR_EQUAL
    | AND
    | OR;
binary_math : PLUS | MINUS | MULTIPLY | DIVIDE | POW;
unary_math : MINUS;

//Variables declaration, initialization & both
var_decl : LET ID (COMMA ID)* COLON type (ASSIGN expr (COMMA expr)*)?;

//Conditional
if_stmt : IF LPAREN expr RPAREN BEGIN stmt* END elif_stmt* else_stmt?;
elif_stmt : ELSEIF LPAREN expr RPAREN BEGIN stmt* END;
else_stmt : ELSE BEGIN stmt* END;

//Loops
for_stmt : FOR ID IN range BEGIN stmt* END;
while_stmt : WHILE expr BEGIN stmt* END;

// Functions
fn_call : ID LPAREN (expr (COMMA expr)*)? RPAREN;
fn_param : ID COLON type;
fn_decl : FN ID LPAREN (fn_param (COMMA fn_param)*)? RPAREN ARROW type BEGIN stmt* END;
return : RETURN expr?;


// Standard library
print_fn : 'print' LPAREN (expr (COMMA expr)*)? RPAREN SEMICOLON;
println_fn : 'println' LPAREN (expr (COMMA expr)*)? RPAREN SEMICOLON;


// Lexer

//KEYWORDS
BEGIN         : '{';
END           : '}';
INT           : 'int';
BOOL          : 'bool';
SET           : 'set';
IF            : 'if';
ELSE          : 'else';
ELSEIF : 'else if';
FOR           : 'for';
WHILE         : 'while';
RETURN        : 'return';
FN : 'fn';
LET : 'let';
TRUE : 'true';
FALSE : 'false';
IN : 'in';

ID            : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [1-9][0-9]* | [0] ;
WS            : [ \n\t\r]+ -> skip;

LPAREN            : '(';
RPAREN           : ')';
LBRACKET     : '[';
RBRACKET    : ']';
COLON : ':';
ARROW : '->';
SEMICOLON : ';';
COMMA           : ',' ;

PLUS            : '+' ;
MINUS           : '-' ;
MULTIPLY        : '*' ;
DIVIDE          : '/' ;
POW : '^';

ASSIGN          : '=';
RANGE : '..';

NEGATION        : '!';
EQUAL           : '==';
NON_EQUAL       : '!=';
LESS            : '<';
GREATER         : '>';
LESS_OR_EQUAL   : '<=';
GREATER_OR_EQUAL : '>=';
AND : '&';
OR : '|';

