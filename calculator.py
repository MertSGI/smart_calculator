
import operator
import re
from string import ascii_letters, digits
from typing import Callable, ClassVar, Dict, List, Pattern, Union

BinaryOperator = Callable[[float, float], float]
BinaryOperators = Dict[str, BinaryOperator]
UnaryOperator = Callable[[float], float]
UnaryOperators = Dict[str, UnaryOperator]


class InvalidExpression(SyntaxError):
    pass


class InvalidIdentifier(SyntaxError):
    pass


class UnknownVariable(NameError):
    pass


class Calculator:
    """Smart Calculator

    description: https://hyperskill.org/projects/74

    P.S. NO `eval`
    """

    supported_operators: ClassVar[Pattern] = re.compile(r'\s*([-+/*^()=])\s*')

    precedence: ClassVar[Dict[str, int]] = {
        r'-': 1,
        r'+': 1,
        r'/': 2,
        r'*': 2,
        r'^': 3,
    }

    binary_operators: ClassVar[BinaryOperators] = {
        r'-': operator.sub,
        r'+': operator.add,
        r'/': operator.truediv,
        r'*': operator.mul,
        r'^': operator.pow,
    }
    unary_operators: ClassVar[UnaryOperators] = {
        r'-': operator.neg,
        r'+': operator.pos,
    }

    def __init__(self) -> None:
        self._variables: Dict[str, float] = dict()

    @staticmethod
    def help():
        print(
            "The program calculates string with addition '+', "
            "subtraction '-', multiplication '*', integer division '/' and"
            " power '^' binary operators and parentheses (...). "
            "It also support unary operators ('-', '+') before numbers."
            " Example:\n"
            ">  - -3-+- 8 *( ( 2^ 2 + 3 ^1)* 2 + 1) + - 6 / (3^3 - 8 *3 )"
            "\n121\n\nSupported commands:\n/help\n/variables"
        )
