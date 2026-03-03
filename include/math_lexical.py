import re
from enum import Enum
from include.data_types import FactorisedNumber, Term
from include.generators.factorize_smarter import FactorizeSmarter


class transcendental_functions(Enum):
    SIN = "sin"
    COS = "cos"
    TAN = "tan"
    LOG = "log"
    E = "e"


class operators(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "**"

class special_characters(Enum):
    OPEN_PARENTHESIS = "("
    CLOSE_PARENTHESIS = ")"
    OPEN_SQUARE_BRACKET = "["
    CLOSE_SQUARE_BRACKET = "]"
    OPEN_CURLY_BRACKET = "{"
    CLOSE_CURLY_BRACKET = "}"
    SPACE = " "

"""
This is a lexical that converts a mathematical equation as a string and builds it into a tree structure of terms

"""




class MathLexical:
    def __init__(self):
        self.fz = FactorizeSmarter()
    def is_number(self, number: str):
        try:
            int(number)
            return True
        except ValueError:
            return False
    def is_float(self, number: str):
        try:
            float(number)
            return True
        except ValueError:
            return False
    def decode(self, expression: str):
        level = 0
        lexical = { 0: []
        }

        equation = list[Term]
        numerator = True #Keeps track of if we are currently working on numerator or denominator
        lexeme = ""
        term = Term()
        for pos, char in enumerate(expression):

            match char:
                case " ":
                    print(f"At {pos} lexeme {lexeme} ({len(lexeme)}), char '{char}' with level {level}")
                    if len(lexeme) > 0:
                        print(f"Adding {lexeme} to lexical")
                        print(lexical)
                        lexical[level].append(lexeme)
                        if self.is_number(lexeme):
                            print(f"{lexeme} is a number, adding to term")
                            number = self.fz.factoize(int(lexeme))
                            if numerator:
                                term.coefficient_numerator = number
                            elif not numerator:
                                term.coefficient_denominator = number
                            print(f"Term: {term}")
                    lexeme = ""
                case "(":
                    if len(lexeme) > 0:
                        print(f"Adding {lexeme} to lexical")
                        lexical[level].append(lexeme)

                    level += 1
                    lexical[level] = []
                    lexeme = ""
                case ")":
                    if len(lexeme) > 0:
                        print(f"Adding {lexeme} to lexical")
                        lexical[level].append(lexeme)
                    level -= 1
                    lexeme = ""
                case _:
                    lexeme += char
        if len(lexeme) > 0:
            print(f"Adding {lexeme} to lexical")
            lexical[level].append(lexeme)

        print(lexical)





if __name__ == "__main__":
    test_equation = "0.5 sin (x ** (1/2)) + 2"
    print(test_equation)
    ml = MathLexical()
    ml.decode(test_equation)