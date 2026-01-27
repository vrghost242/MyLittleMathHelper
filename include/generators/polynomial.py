from fractions import Fraction
import random
from typing import Literal, Optional
from pydantic import BaseModel
from matplotlib.pyplot as plt
import sympy


def pr_frac(fraction: Fraction):
    if fraction < 0:
        return str(f"- {Fraction(fraction*-1)}")
    return str(f"+ {Fraction(fraction)}")

def rand_fraction(range: tuple[Fraction, Fraction]):
    denominator = random.randint(int(range[0]), int(range[1]))
    numerator = random.randint(int(range[0]), int(range[1]))
    return Fraction(numerator, abs(denominator))

class polynomial_cube(BaseModel):
    '''
     Simple class for storing a polynoial of the form ax^2+bx+c, it also supports storing the sum
    '''
    coefficient: Fraction = Fraction(1)
    first: Fraction
    second: Fraction
    result_value: Optional[Fraction] = None

    def get_polynomial(self):
        if self.coefficient == 1:
            x2_string= "x^2"
        else:
            x2_string = f"{pr_frac(self.coefficient) }x^2"
        return f"{x2_string} {pr_frac((self.first+self.second)*self.coefficient)}x {pr_frac((self.first*self.second)* self.coefficient)}"

    def get_completed_square(self):
        return f"(x + {self.first})(x + {self.second})"


default_range = ("-10", "10")

def univariate_polynomial(index_coeffificents: list[ Fraction], indexies: Literal[list[Fraction] | None] = None):
    for i in index_coeffificents:
        print(Fraction(i))
    pass

def rand_int(range: tuple[Fraction, Fraction]):
    integer =random.randint( int(range[0]), int(range[1]) )
    return Fraction(
        str(integer)
    )


def monic_univariate_polynomial(range: tuple[Fraction, Fraction]=default_range, coefficient: Fraction = Fraction(1), int_only: bool = True):
    rand = random.seed()
    if int_only:
        q= rand_int(range)
        r= rand_int(range)
    else:
        q = rand_fraction(range)
        r = rand_fraction(range)
    resp = polynomial_cube(
        coefficient= coefficient,
        first= q,
        second= r
    )
    return resp




def random_univariate_polynomial(complexity: int = 1, range: tuple[Fraction, Fraction]=default_range):
    polynomial = monic_univariate_polynomial(range)
    print("This is your Polynomial:")
    print(polynomial.get_polynomial())
    input("Press enter to continue")
    print(polynomial.get_completed_square())
    polynomial = monic_univariate_polynomial(range, int_only=False)
    print("This is your Polynomial:")
    print(polynomial.get_polynomial())
    input("Press enter to continue")
    print(polynomial.get_completed_square())






if __name__ == '__main__':
    random_univariate_polynomial()
