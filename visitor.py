import antlr4.tree
import antlr4.tree.TokenTagToken
import antlr4.tree.Tree
from dust_grammar.DustGrammarVisitor import DustGrammarVisitor
from dust_grammar.DustGrammarParser import DustGrammarParser
import antlr4
from dataclasses import dataclass
from typing import Literal

class DustVisitor(DustGrammarVisitor):
    def __init__(self):
        self.output = []
        self.symbol_table = {}  # Таблица символов для проверки переменных
        self.functions = {}  # Таблица функций для проверки сигнатур
        self._tabs = 0
        self._errors: list[str] = []
    
    def add_function(self, ctx, name, signature, return_type):
        """Добавить функцию с сигнатурой и проверкой перегрузки."""
        if name not in self.functions:
            self.functions[name] = {}
        if signature in self.functions[name]:
            self._add_error(ctx, f"Function {name} with signature {signature} already defined.")
        self.functions[name][signature] = return_type
    
    def _add_error(self, ctx, error: str) -> None:
        self._errors.append(f'\033[31;1mSemantic error\033[0m: Line {ctx.start.line} Column {ctx.start.column} - {error.capitalize()}')
    
    def _add_tabs(self):
        return ' ' * 4 * self._tabs
    
    def visitProgram(self, ctx: DustGrammarParser.ProgramContext):
        # self.output.append("from numba import njit\n\n")
        with open('set.py') as file:
            self.output.append(f'{file.read()}\n')
        self.visitChildren(ctx)
        return "\n".join(self.output)

    def visitFn_decl(self, ctx: DustGrammarParser.Fn_declContext):
        # Получаем имя функции
        name = ctx.ID().getText()

        # Получаем список параметров и их типы
        params = []
        param_types = []
        if ctx.fn_param():
            for param in ctx.fn_param():
                param_name = param.ID().getText()
                param_type = self.visit(param.type_())  # Тип параметра
                params.append((param_name, param_type))
                param_types.append(param_type)

        # Получаем возвращаемый тип
        return_type = self.visit(ctx.type_())  # Тип возвращаемого значения

        # Проверяем перегрузку функции
        self.add_function(ctx, name, tuple(param_types), return_type)

        # Обновляем таблицу символов: параметры функции
        old_symbol_table = self.symbol_table.copy()
        self.symbol_table = {param[0]: param[1] for param in params}

        # Генерация заголовка функции в Python
        python_params = [f"{name}: {type_}" for name, type_ in params]
        self.output.append(f"{self._add_tabs()}def {name}({', '.join(python_params)}):")

        self._tabs += 1
        # Обрабатываем тело функции
        self.visitChildren(ctx)
        self._tabs -= 1

        # Восстанавливаем таблицу символов
        self.symbol_table = old_symbol_table        

        self.output.append("")  # Пустая строка после функции

    def visitMain_fn(self, ctx: DustGrammarParser.Main_fnContext):
        self.output.append("if __name__ == '__main__':")
        self._tabs += 1        
        self.visitChildren(ctx)
        self._tabs -= 1
        self.output.append("\n")

    def visitVar_decl(self, ctx: DustGrammarParser.Var_declContext):
        # Получаем список имен переменных
        var_names = [id_token.getText() for id_token in ctx.ID()]

        # Получаем тип переменной
        var_type = self.visit(ctx.type_())

        # Обрабатываем выражение(я) и сохраняем результат
        expr_values = [self.visit(expr) for expr in ctx.expr()]

        # Проверяем, что количество переменных совпадает с количеством выражений
        if len(var_names) != len(expr_values):
            error_text = (f"Mismatch between the number of variables and expressions: "
                          f"{len(var_names)} variables and {len(expr_values)} expressions.")
            self._add_error(ctx, error_text)

        for var_name, expr_value in zip(var_names, expr_values):
            # # Проверяем, что переменная еще не объявлена
            # if var_name in self.symbol_table:
            #     raise Exception(f"Variable {var_name} already defined.")

            # Добавляем переменную в таблицу символов
            self.symbol_table[var_name] = var_type

            # Генерируем строку для вывода в Python
            self.output.append(f"{self._add_tabs()}{var_name} = {expr_value}")

        return var_names

    def visitAssign(self, ctx: DustGrammarParser.AssignContext):
        ids = [id_.getText() for id_ in ctx.ID()]
        exprs = [self.visit(expr) for expr in ctx.expr()]
        for id_ in ids:
            if id_ not in self.symbol_table:
                self._add_error(ctx, f"Variable \'{id_}\' is not defined.")
        self.output.append(f"{self._add_tabs()}{', '.join(ids)} = {', '.join(exprs)}")

    def visitIf_stmt(self, ctx: DustGrammarParser.If_stmtContext):
        # Получаем условие if
        cond = self.visit(ctx.expr())
        self.output.append(f"{self._add_tabs()}if {cond}:")
        
        # Обрабатываем все операторы внутри if
        self._tabs += 1
        for stmt in ctx.stmt():
            self.visit(stmt)
        self._tabs -= 1
        
        # Обрабатываем все elif (если есть)        
        for elif_ctx in ctx.elif_stmt():
            self.visit(elif_ctx)        

        # Обрабатываем else (если есть)        
        if ctx.else_stmt():
            self.visit(ctx.else_stmt())        


    def visitElif_stmt(self, ctx: DustGrammarParser.Elif_stmtContext):
        cond = self.visit(ctx.expr())
        self.output.append(f"{self._add_tabs()}elif {cond}:")
        self._tabs += 1
        for stmt in ctx.stmt():
            self.visit(stmt)
        self._tabs -= 1

    def visitElse_stmt(self, ctx: DustGrammarParser.Else_stmtContext):
        self.output.append(f"{self._add_tabs()}else:")
        self._tabs += 1
        for stmt in ctx.stmt():
            self.visit(stmt)
        self._tabs -= 1

    def visitFor_stmt(self, ctx: DustGrammarParser.For_stmtContext):
        loop_var = ctx.ID().getText()
        
        # Проверка на уже существующую переменную
        if loop_var in self.symbol_table:
            raise self._add_error(ctx, f"Variable \'{loop_var}\' is already defined.")
        
        # Обработка выражения range
        range_expr = self.visit(ctx.range_())  # Получаем диапазон целиком
        self.symbol_table[loop_var] = "int"   # Добавляем переменную в таблицу символов
        
        # Формирование эквивалента Python-кода
        self.output.append(f"{self._add_tabs()}for {loop_var} in {range_expr}:")
        
        # Обработка тела цикла
        self._tabs += 1
        for stmt in ctx.stmt():
            self.visit(stmt)
        self._tabs -= 1

    def visitWhile_stmt(self, ctx: DustGrammarParser.While_stmtContext):
        cond = self.visit(ctx.expr())
        self.output.append(f"{self._add_tabs()}while {cond}:")
        self._tabs += 1
        for stmt in ctx.stmt():
            self.visit(stmt)
        self._tabs -= 1

    def visitPrint_fn(self, ctx):
        # Обрабатываем аргументы print
        args = []
        for expr in ctx.expr():            
            arg = self.visit(expr)
            if arg is None:
                self._add_error(ctx, f"Failed to evaluate expression in print: {expr.getText()}")
            args.append(arg)

        # Формируем Python-код для print
        self.output.append(f"{self._add_tabs()}print({', '.join(args)}, end='')")

        return None

    def visitPrintln_fn(self, ctx: DustGrammarParser.Println_fnContext):
        args = [self.visit(expr) for expr in ctx.expr()]
        self.output.append(f"{self._add_tabs()}print({', '.join(args)})")

    def visitExpr(self, ctx: DustGrammarParser.ExprContext):
        if ctx.atom():
            return self.visit(ctx.atom())
        elif ctx.binary_math():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.binary_math().getText()
            return f"({left} {op} {right})"
        elif ctx.binary_logical():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.binary_logical().getText()
            return f"({left} {op} {right})"
        elif ctx.unary_math():
            expr = self.visit(ctx.expr(0))
            op = ctx.unary_math().getText()
            return f"({op}{expr})"
        elif ctx.set_():            
            return self.visit(ctx.set_())
        elif ctx.fn_call():  # Обработка вызова функции
            return self.visit(ctx.fn_call())  # Перенаправляем к visitFn_call


    def visitAtom(self, ctx: DustGrammarParser.AtomContext):
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.symbol_table:
                self._add_error(ctx, f"Variable {var_name} not defined.")
            return var_name
        elif ctx.literal():
            return self.visit(ctx.literal())

    def visitLiteral(self, ctx: DustGrammarParser.LiteralContext):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.TRUE():
            return "True"
        elif ctx.FALSE():
            return "False"

    def visitSet(self, ctx: DustGrammarParser.SetContext):
        elements = [self.visit(expr) for expr in ctx.expr()]
        return f"WrappedSet([{', '.join(elements)}])"

    def visitRange(self, ctx: DustGrammarParser.RangeContext):
        start = self.visit(ctx.expr(0))
        end = self.visit(ctx.expr(1))
        return f"range({start}, {end})"

    def visitFn_call(self, ctx: DustGrammarParser.Fn_callContext):
        fn_name = ctx.ID().getText()
        # Получаем аргументы и их типы
        args = [self.visit(expr) for expr in ctx.expr()]
        arg_types = [self.get_expr_type(expr) for expr in ctx.expr()]        

        # Проверяем, есть ли вообще такая функция
        if fn_name not in self.functions:
            self._add_error(ctx, f"Function \'{fn_name}\' is not defined.")
            return ""
        
        # Проверяем, есть ли такая функция
        if tuple(arg_types) not in self.functions[fn_name]:
            self._add_error(ctx, f"Function {fn_name} with signature {arg_types} not defined.")
        
        # Возвращаем результат вызова функции
        return f"{fn_name}({', '.join(args)})"

    def get_expr_type(self, expr):
        """Определение типа выражения для проверки сигнатур функций."""
        if expr.atom():
            if expr.atom().ID():
                return self.symbol_table[expr.atom().ID().getText()]
            elif expr.atom().literal():
                literal = expr.atom().literal()
                if literal.NUMBER():
                    return "int"
                elif literal.TRUE() or literal.FALSE():
                    return "bool"
        elif expr.set_():
            return "WrappedSet"
        elif expr.binary_math() or expr.unary_math():
            return "int"
        elif expr.binary_logical() or expr.unary_logical():
            return "bool"
        # Добавить другие типы по необходимости
        return "unknown"

    def visitReturn(self, ctx: DustGrammarParser.ReturnContext):
        if ctx.expr():
            expr = self.visit(ctx.expr())
            return_type = self.get_expr_type(ctx.expr())
            # Здесь можно проверить, соответствует ли тип возвращаемого значения типу функции
            self.output.append(f"{self._add_tabs()}return {expr}")
        else:
            self.output.append(f"{self._add_tabs()}return")

    def visitStmt(self, ctx: DustGrammarParser.StmtContext):
        if ctx.expr():
            self.visit(ctx.expr())
        elif ctx.assign():
            self.visit(ctx.assign())
        elif ctx.var_decl():
            self.visit(ctx.var_decl())
        elif ctx.return_():
            self.visit(ctx.return_())
        elif ctx.if_stmt():
            self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            self.visit(ctx.for_stmt())
        elif ctx.while_stmt():
            self.visit(ctx.while_stmt())
        elif ctx.print_fn():
            self.visit(ctx.print_fn())
        elif ctx.println_fn():
            self.visit(ctx.println_fn())

    def visitUnary_math(self, ctx: DustGrammarParser.Unary_mathContext):
        op = ctx.getText()
        return op

    def visitBinary_math(self, ctx: DustGrammarParser.Binary_mathContext):
        return ctx.getText()

    def visitUnary_logical(self, ctx: DustGrammarParser.Unary_logicalContext):
        return ctx.getText()

    def visitBinary_logical(self, ctx: DustGrammarParser.Binary_logicalContext):
        return ctx.getText()    
    
    def visitType(self, ctx: DustGrammarParser.TypeContext):
        if ctx.INT():
            return "int"
        elif ctx.BOOL():
            return "bool"
        elif ctx.SET():
            return "set"
        else:
            self._add_error(ctx, f"Unknown type: {ctx.getText()}")
    
    @property
    def code(self) -> str:
        return '\n'.join(self.output)
    
    @property
    def errors(self) -> list[str]:
        return self._errors
