# Generated from DustGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DustGrammarParser import DustGrammarParser
else:
    from DustGrammarParser import DustGrammarParser

# This class defines a complete generic visitor for a parse tree produced by DustGrammarParser.

class DustGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DustGrammarParser#program.
    def visitProgram(self, ctx:DustGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#type.
    def visitType(self, ctx:DustGrammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#literal.
    def visitLiteral(self, ctx:DustGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#set.
    def visitSet(self, ctx:DustGrammarParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#atom.
    def visitAtom(self, ctx:DustGrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#range.
    def visitRange(self, ctx:DustGrammarParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#main_fn.
    def visitMain_fn(self, ctx:DustGrammarParser.Main_fnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#expr.
    def visitExpr(self, ctx:DustGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#stmt.
    def visitStmt(self, ctx:DustGrammarParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#assign.
    def visitAssign(self, ctx:DustGrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#unary_logical.
    def visitUnary_logical(self, ctx:DustGrammarParser.Unary_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#binary_logical.
    def visitBinary_logical(self, ctx:DustGrammarParser.Binary_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#binary_math.
    def visitBinary_math(self, ctx:DustGrammarParser.Binary_mathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#unary_math.
    def visitUnary_math(self, ctx:DustGrammarParser.Unary_mathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#var_decl.
    def visitVar_decl(self, ctx:DustGrammarParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#if_stmt.
    def visitIf_stmt(self, ctx:DustGrammarParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#elif_stmt.
    def visitElif_stmt(self, ctx:DustGrammarParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#else_stmt.
    def visitElse_stmt(self, ctx:DustGrammarParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#for_stmt.
    def visitFor_stmt(self, ctx:DustGrammarParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#while_stmt.
    def visitWhile_stmt(self, ctx:DustGrammarParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#fn_call.
    def visitFn_call(self, ctx:DustGrammarParser.Fn_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#fn_param.
    def visitFn_param(self, ctx:DustGrammarParser.Fn_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#fn_decl.
    def visitFn_decl(self, ctx:DustGrammarParser.Fn_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#return.
    def visitReturn(self, ctx:DustGrammarParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#print_fn.
    def visitPrint_fn(self, ctx:DustGrammarParser.Print_fnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DustGrammarParser#println_fn.
    def visitPrintln_fn(self, ctx:DustGrammarParser.Println_fnContext):
        return self.visitChildren(ctx)



del DustGrammarParser