from fractions import Fraction
from collections import Counter
import math
from sympy.parsing.sympy_parser import null

from include.logger import Logger
from sympy import roots
from fractions import Fraction
from factorize_smarter import FactorisedNumber, FactorizeSmarter



log = Logger("roots")
logLevel = "DEBUG"

class Root:
    def __init__(self):
        self.fz = FactorizeSmarter()
    def prime_roots(self, radicand: int|FactorisedNumber|Fraction|float, radical_index: int = 2):
        if isinstance(radicand, int):
            radicand = self.fz.factoize(radicand)
        elif isinstance(radicand, Fraction):
            log.warning(f"Converting Fractions not implemented yet")
            log.warning(f"Converting {radicand} to {int(radicand)}")
            radicand = self.fz.factoize(int(radicand))
        elif isinstance(radicand, float):
            log.warning(f"Converting floats not implemented yet")
            return None

        log.debug(f"Calculating roots of {radicand.factors} ({radicand.value})")
        prime_roots: list[int] = []
        prime_leftovers: list[int] = []

        # Lets find any ocurences where the radicand have a set of prime factors matching the radical_index, I.E, 4 have 2 2 (so 2 occarnaces od prime 2)
        prime_groups = Counter(radicand.factors)
        for i in prime_groups:
            if prime_groups[i]//radical_index > 0:
                log.debug(f"Found a prime group of {i} with {prime_groups[i]//radical_index} occurences of groups of {radical_index}")
                for r in range(0, prime_groups[i]//radical_index):
                    prime_roots.append(i)
                if prime_groups[i]%radical_index:
                    log.debug(f"Leftover after found root is {prime_groups[i]%radical_index} for {radical_index}")
                    for l in range(0, prime_groups[i]%radical_index):
                        prime_leftovers.append(i)
            else:
                log.debug(f"Leftover is {i}: {prime_groups[i]}")
                for l in range(0, prime_groups[i]):
                    prime_leftovers.append(i)
        log.debug(f"Prime roots found for radical index {radical_index} are {prime_roots}")
        log.debug(f"Prime {radical_index} roots are {prime_roots}")
        if len(prime_leftovers)> 0:
            log.debug(f"Leftover roots are {prime_leftovers}")
        log.info(f"Calculated roots for radical index {radical_index} from {radicand.value} extracted integers {math.prod(prime_roots)} and {math.prod(prime_leftovers)} leftovers")
        return math.prod(prime_roots), math.prod(prime_leftovers)








if __name__ == "__main__":
    log.debug("Hello World")
    root = Root()
    root.prime_roots(180)
    root.prime_roots(256,3)
    root.prime_roots(8, 2)