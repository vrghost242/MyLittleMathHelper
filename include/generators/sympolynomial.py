from fractions import Fraction
import random
from typing import Literal, Optional
from pydantic import BaseModel
import matplotlib.pyplot as plt
from sympy import sqrt, Symbol, simplify, latex, Function


class polynomial():
    def __init__(self,
                 p: Fraction = None,
                 q: Fraction = None,
                 coefficient: Fraction = Fraction(1),
                 symbol_to_use: str = "x"):
        self.x = Symbol(symbol_to_use)
        print(type(self.x))
        print(simplify(sqrt(self.x**2)))
        y = Function("f")(=2*self.x**2+5*self.x+20)
        lat = latex(y)

        # add text
        plt.text(0, 0.6, r"$%s$" % lat, fontsize=50)

        # hide axes
        fig = plt.gca()
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.draw()  # or savefig
        plt.show()



if __name__ == '__main__':
    pol = polynomial()