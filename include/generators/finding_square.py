from collections import Counter
from fractions import Fraction
from timeit import default_timer as timer
from include.logger import Logger
from include.generators.roots import Root
from include.generators.factorize_smarter import FactorisedNumber, FactorizeSmarter
import math



log = Logger("squares")
LOG_LEVEL = "DEBUG"
fz = FactorizeSmarter()
root = Root()

class FindingSquare:
    def _permutation_loop(self, factorlist: list, t1_length: int):
        log = Logger(f'_PERMUTATION {t1_length}')
        log.console.setLevel(LOG_LEVEL)
        last_factor = 1
        for i in range(0, len(factorlist)):
            _cur_list = factorlist.copy()
            term_1 = _cur_list.pop(i)
            log.debug(f"t1_length {i}/{len(_cur_list) - 1}: {term_1}")

            if term_1 == last_factor:
                log.debug(f"Skipping {i} {term_1} as it is the same as last factor {last_factor}")
                continue
            else:
                last_factor = term_1

                yield (term_1, math.prod(_cur_list))

                if t1_length > 1:
                    log.debug(f"Recursing with {t1_length - 1} factors left")
                    for _child_pair in self._permutation_loop(_cur_list, t1_length - 1):
                        yield term_1 * _child_pair[0], _child_pair[1]

    def permutator(self, factorlist: list):
        log=Logger('PERMUTATOR')
        log.console.setLevel(LOG_LEVEL)
        last_term = 1
        permutations = 1
        # Lets first sort out 1, as that is always an option
        yield (1, math.prod(factorlist))
        for t1_length in range(1, (len(factorlist) // 2) + 1):
            log.info(f"Starting permutation loop with {t1_length} / {len(factorlist) // 2} factors left")
            yield from self._permutation_loop(factorlist, t1_length)

    def find_sum_product_pair_by_primes(self, sum: int | Fraction | FactorisedNumber, product: int | Fraction | FactorisedNumber) -> \
    tuple[Fraction, Fraction]:
        log=Logger('PRODUCT PAIR')
        log.console.setLevel(LOG_LEVEL)
        # First lets make certain we have a factorised number
        if isinstance(sum, Fraction) | isinstance(product, int):
            product = fz.factoize(product)
        if isinstance(product, Fraction) | isinstance(sum, int):
            sum = fz.factoize(sum)

        log.debug(f"Sum: {sum.value} factors {sum.factors}")
        log.debug(f"Product: {product.value} factors {product.factors}")

        # Identify if both have the same sign (positive or negative)
        if product.value > 0:
            log.debug("As product is positive, the terms must be added and both terms must have same number")
            target = abs(sum.value)
            log.debug(f"Target {target}")
            for terms in self.permutator(product.factors):
                term1 = terms[0]
                term2 = terms[1]
                if term1 + term2 == target:
                    if sum.value < 0:
                        log.debug("Sum is negative, so both sums must be negative")
                        term1 = term1 * -1
                        term2 = term2 * -1
                    log.debug(
                        f"Found a pair {term1} + {term2} = {sum.value} and {term1} * {term2} = {product.value}")
                    return Fraction(term1), Fraction(term2)
            return Fraction(0), Fraction(0)
        elif product.value < 0:
            log.debug(
                "Product is negative, so we will need to subtrack one term from the other, so we +term1 -term2")
            target = sum.value
            log.debug(f"Target {target}")
            for terms in self.permutator(product.factors):
                term1 = terms[0]
                term2 = terms[1]
                log.debug(f"Trying {term1} - {term2} = {term1 - term2} (Target{target})")
                if term1 - term2 == target:
                    log.debug(
                        f"Found a pair {term1} - {term2} = {sum.value} and {term1} * {term2} = {product.value}")
                    return Fraction(term1), Fraction(-term2)
                if term2 - term1 == target:
                    log.debug(
                        f"Found a pair {term2} - {term1} = {sum.value} and {term1} * {term2} = {product.value}")
                    return Fraction(-term1), Fraction(term2)
            return Fraction(0), Fraction(0)
        if sum.value < 0 and product.value < 0:
            pass

    def find_sum_product_pair_by_math(self, sum: int | Fraction | FactorisedNumber, product: int | Fraction | FactorisedNumber) -> \
    tuple[Fraction, Fraction]:
        '''
        We are looking for two values, that must follow the pattern
        sum = (p - q)+(p + q)
        We also know that
        product = (p - q)*(p + q) = (p + q) * (p - q) = (p - q)^2
        Hence we can also say that p must be sum/2, so lets calculate it
        :param sum:
        :param product:
        :return:
        '''
        log=Logger('CALC PAIR')
        log.console.setLevel('DEBUG')
        # First lets make certain we have a factorised number
        # if isinstance(sum, Fraction) | isinstance(product, int):
        #     product = self.factoize(product)
        # if isinstance(product, Fraction) | isinstance(sum, int):
        #     sum = self.factoize(sum)

        #This is the median between the two points (-b`/2), so b' because X does not get to play at all :)
        m = -sum / 2
        log.debug(f"Found midpoint m = {m}")
        # So lets see what the suare of the difference is
        d2 = m**2 - product
        log.debug(f"Found distane^2 = {d2}")
        d, r = root.prime_roots(abs(d2))
        log.debug(f"Found Distance between the point and midpoint = {d} square root of {r}")
        term1 = sum / 2 - d
        term2 = sum / 2 + d
        log.debug(f"Found terms {term1} and {term2}")
        return Fraction(term1), Fraction(term2)

    def find_square_simpler(self, b_prime: int | Fraction, c_prime: int) -> tuple[Fraction, Fraction]:
        """Finds the square of a number using a simpler method
        Implement b and c prime function based on a (so b' = b/a"""



if __name__ == '__main__':
    sq = FindingSquare()
    fs_first = -603
    fs_second = 1800
    log.info(f"Testing finding sum product pair for {fs_first} and {fs_second}")
    time = timer()
    pair = sq.find_sum_product_pair_by_primes(fs_first, fs_second)
    if pair[0] == 0 and pair[1] == 0:
        log.error(f"Could not find a pair for {fs_first} and {fs_second}")
    else:
        log.info(f"Got the following pair by prime {pair} - Took {timer() - time} seconds")

    fs_first = Fraction('8')
    fs_second = Fraction('12')
    time = timer()
    pair2 = sq.find_sum_product_pair_by_math(fs_first, fs_second)
    log.info(f"Got the following pair by math {pair2} - Took {timer() - time} seconds")

    fs_first = Fraction('603')
    fs_second = Fraction('1800')
    time = timer()
    pair2 = sq.find_sum_product_pair_by_math(fs_first, fs_second)
    log.info(f"Got the following pair by math {pair2} - Took {timer() - time} seconds")