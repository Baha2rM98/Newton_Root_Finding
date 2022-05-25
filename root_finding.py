import sympy as sym
import math
from abc import ABC, abstractmethod
from sympy import Symbol, parse_expr


class IterativeMethods(ABC):
    _sym_symbol = None
    _function = None

    @abstractmethod
    def __init__(self, symbol: str, function: str) -> None:
        self._sym_symbol = Symbol(symbol)
        self._check_function_syntax(function)

    def _check_function_syntax(self, func: str) -> None:
        try:
            self._function = parse_expr(func, evaluate=False)
        except Exception:
            raise SyntaxError('Syntax error in function: ' + func)
        if str(self._function.free_symbols.pop()) != str(self._sym_symbol):
            raise SyntaxError(f'Missmatch symbol {self._sym_symbol} in function: {func}')

    def _reset(self) -> None:
        self._sym_symbol = None
        self._function = None


class NewtonMethod(IterativeMethods):
    __iterations = 0

    def __init__(self, symbol: str, function: str) -> None:
        self._reset()
        super().__init__(symbol, function)

    def __function_value(self, initial_point: float) -> float:
        symbol_val = dict()
        symbol_val[self._sym_symbol] = initial_point
        return self._function.evalf(subs=symbol_val)

    def __function_derivative(self, initial_point: float) -> float:
        symbol_val = dict()
        symbol_val[self._sym_symbol] = initial_point
        return sym.diff(self._function, self._sym_symbol).evalf(subs=symbol_val)

    def __function_second_derivative(self, initial_point: float) -> float:
        symbol_val = dict()
        symbol_val[self._sym_symbol] = initial_point
        return sym.diff(self._function, self._sym_symbol, 2).evalf(subs=symbol_val)

    def newtons_method(self, initial_point: float, epsilon: float = 1e-13) -> None:
        iterative_point = initial_point
        self.__iterations = 0

        while math.fabs(self.__function_value(iterative_point)) > epsilon:
            diff = self.__function_derivative(iterative_point)
            if diff == 0.:
                raise ZeroDivisionError(
                    f'Can not divide by Zero. Derivative of this function at point {initial_point} is Zero.')
            iterative_point = iterative_point - (self.__function_value(iterative_point) / diff)
            self.__iterations += 1
            print('Optimal root: ', iterative_point, '\t', 'In iteration: ', self.__iterations)

        opt_symbol_value = dict()
        opt_symbol_value[self._sym_symbol] = iterative_point

        print('Finished -> [Function value in root point: ' + str(self._function.evalf(subs=opt_symbol_value)) + ']')
        print()

    def newtons_optimization_method(self, initial_point: float, epsilon: float = 1e-13) -> None:
        iterative_point = initial_point
        self.__iterations = 0

        while math.fabs(self.__function_derivative(iterative_point)) > epsilon:
            second_diff = self.__function_second_derivative(iterative_point)
            if second_diff == 0.:
                raise ZeroDivisionError(
                    f'Can not divide by Zero. Second derivative of this function at point {initial_point} is Zero.')
            iterative_point = iterative_point - (self.__function_derivative(iterative_point) / second_diff)
            self.__iterations += 1
            print('Optimal point: ', iterative_point, '\t', 'In iteration: ', self.__iterations)

        opt_symbol_value = dict()
        opt_symbol_value[self._sym_symbol] = iterative_point

        print('Finished -> [Optimal value: ' + str(self._function.evalf(subs=opt_symbol_value)) + ']')
        print()
