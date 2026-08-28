import re
from enum import Enum
from include.data_types import FactorisedNumber, Term
from include.generators.factorize_smarter import FactorizeSmarter


transcendental_functions=[
    "sin",
    "cos",
    "tan",
    "log",
    "e"
]



operators=[
    "+",
    "-",
    "*",
    "/",
    "**"
]


"""
This is a lexical that converts a mathematical equation as a string and builds it into a tree structure of terms

"""

def next_alpha(s):
    return chr(ord(s) + 1)

def is_number(number: str):
    try:
        int(number)
        return True
    except ValueError:
        return False

def is_float(number: str):
    try:
        float(number)
        return True
    except ValueError:
        return False

def is_transendent_function(term: str):
    if term in transcendental_functions:
        return True
    else:
        return False

def argument_type(arg: str):
    if arg in operators:
        return "OPERATOR"
    elif arg in transcendental_functions:
        return "TRANSCENDENT"
    elif is_number(arg):
        return "NUMBER"
    elif is_float(arg):
        return "FLOAT"

class MathLexical:
    def __init__(self):
        self.fz = FactorizeSmarter()

    def compile(self, function: list, functionid: str):
        print(f"Compiling {function}")

        # Lets first break up if someone has not left any space between opperators
        _function = []

        print(f"Compiling {_function}")
        arg_type_list = []
        for arg in _function:
            print(f"Compiling {arg}")
            arg_type_list.append(argument_type(arg))

        match arg_type_list:
            case [ "NUMBER", "OPERATOR", "NUMBER"]:
                print("You just sent a factor")
            case _:
                print(f"You send {arg_type_list}")
        # Lets figure out if we have any variables or trancendental functions



        return(f"{functionid}(x)")
    def decode(self, expression: str):
        level = 0
        lexical = { 0: []
        }
        functionid = "f"
        equation = list[Term]
        numerator = True #Keeps track of if we are currently working on numerator or denominator
        lexeme = ""
        term = Term()
        for pos, char in enumerate(expression):

            match char:
                case " ":

                    if len(lexeme) > 0:

                        print(lexical)
                        lexical[level].append(lexeme)
                        if is_number(lexeme):

                            number = self.fz.factoize(int(lexeme))
                            if numerator:
                                term.coefficient_numerator = number
                            elif not numerator:
                                term.coefficient_denominator = number
                            print(f"Term: {term}")
                    lexeme = ""
                case "(":
                    if len(lexeme) > 0:

                        lexical[level].append(lexeme)

                    level += 1
                    lexical[level] = []
                    lexeme = ""
                case ")":
                    if len(lexeme) > 0:

                        lexical[level].append(lexeme)
                    function = self.compile(lexical[level], functionid)
                    functionid = next_alpha(functionid)
                    level -= 1
                    lexical[level].append(function)
                    lexeme = ""
                case _:
                    lexeme += char
        if len(lexeme) > 0:

            lexical[level].append(lexeme)

        print(lexical)





if __name__ == "__main__":
    test_equation = "0.5 sin (x ** (1/2)) + 2"
    print(test_equation)
    ml = MathLexical()
    ml.decode(test_equation)