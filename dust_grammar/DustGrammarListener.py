# Generated from DustGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DustGrammarParser import DustGrammarParser
else:
    from DustGrammarParser import DustGrammarParser

# This class defines a complete listener for a parse tree produced by DustGrammarParser.
class DustGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by DustGrammarParser#program.
    def enterProgram(self, ctx:DustGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#program.
    def exitProgram(self, ctx:DustGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#type.
    def enterType(self, ctx:DustGrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#type.
    def exitType(self, ctx:DustGrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#literal.
    def enterLiteral(self, ctx:DustGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#literal.
    def exitLiteral(self, ctx:DustGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#set.
    def enterSet(self, ctx:DustGrammarParser.SetContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#set.
    def exitSet(self, ctx:DustGrammarParser.SetContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#atom.
    def enterAtom(self, ctx:DustGrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#atom.
    def exitAtom(self, ctx:DustGrammarParser.AtomContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#range.
    def enterRange(self, ctx:DustGrammarParser.RangeContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#range.
    def exitRange(self, ctx:DustGrammarParser.RangeContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#main_fn.
    def enterMain_fn(self, ctx:DustGrammarParser.Main_fnContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#main_fn.
    def exitMain_fn(self, ctx:DustGrammarParser.Main_fnContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#expr.
    def enterExpr(self, ctx:DustGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#expr.
    def exitExpr(self, ctx:DustGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#stmt.
    def enterStmt(self, ctx:DustGrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#stmt.
    def exitStmt(self, ctx:DustGrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#assign.
    def enterAssign(self, ctx:DustGrammarParser.AssignContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#assign.
    def exitAssign(self, ctx:DustGrammarParser.AssignContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#unary_logical.
    def enterUnary_logical(self, ctx:DustGrammarParser.Unary_logicalContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#unary_logical.
    def exitUnary_logical(self, ctx:DustGrammarParser.Unary_logicalContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#binary_logical.
    def enterBinary_logical(self, ctx:DustGrammarParser.Binary_logicalContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#binary_logical.
    def exitBinary_logical(self, ctx:DustGrammarParser.Binary_logicalContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#binary_math.
    def enterBinary_math(self, ctx:DustGrammarParser.Binary_mathContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#binary_math.
    def exitBinary_math(self, ctx:DustGrammarParser.Binary_mathContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#unary_math.
    def enterUnary_math(self, ctx:DustGrammarParser.Unary_mathContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#unary_math.
    def exitUnary_math(self, ctx:DustGrammarParser.Unary_mathContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#var_decl.
    def enterVar_decl(self, ctx:DustGrammarParser.Var_declContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#var_decl.
    def exitVar_decl(self, ctx:DustGrammarParser.Var_declContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#if_stmt.
    def enterIf_stmt(self, ctx:DustGrammarParser.If_stmtContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#if_stmt.
    def exitIf_stmt(self, ctx:DustGrammarParser.If_stmtContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#elif_stmt.
    def enterElif_stmt(self, ctx:DustGrammarParser.Elif_stmtContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#elif_stmt.
    def exitElif_stmt(self, ctx:DustGrammarParser.Elif_stmtContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#else_stmt.
    def enterElse_stmt(self, ctx:DustGrammarParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#else_stmt.
    def exitElse_stmt(self, ctx:DustGrammarParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#for_stmt.
    def enterFor_stmt(self, ctx:DustGrammarParser.For_stmtContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#for_stmt.
    def exitFor_stmt(self, ctx:DustGrammarParser.For_stmtContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#while_stmt.
    def enterWhile_stmt(self, ctx:DustGrammarParser.While_stmtContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#while_stmt.
    def exitWhile_stmt(self, ctx:DustGrammarParser.While_stmtContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#fn_call.
    def enterFn_call(self, ctx:DustGrammarParser.Fn_callContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#fn_call.
    def exitFn_call(self, ctx:DustGrammarParser.Fn_callContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#fn_param.
    def enterFn_param(self, ctx:DustGrammarParser.Fn_paramContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#fn_param.
    def exitFn_param(self, ctx:DustGrammarParser.Fn_paramContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#fn_decl.
    def enterFn_decl(self, ctx:DustGrammarParser.Fn_declContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#fn_decl.
    def exitFn_decl(self, ctx:DustGrammarParser.Fn_declContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#return.
    def enterReturn(self, ctx:DustGrammarParser.ReturnContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#return.
    def exitReturn(self, ctx:DustGrammarParser.ReturnContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#print_fn.
    def enterPrint_fn(self, ctx:DustGrammarParser.Print_fnContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#print_fn.
    def exitPrint_fn(self, ctx:DustGrammarParser.Print_fnContext):
        pass


    # Enter a parse tree produced by DustGrammarParser#println_fn.
    def enterPrintln_fn(self, ctx:DustGrammarParser.Println_fnContext):
        pass

    # Exit a parse tree produced by DustGrammarParser#println_fn.
    def exitPrintln_fn(self, ctx:DustGrammarParser.Println_fnContext):
        pass



del DustGrammarParser