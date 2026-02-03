import math
import json

from numpy.ma.core import absolute

from include.logger import Logger

import sys
from pydantic import BaseModel, Field
from collections import Counter
from fractions import Fraction
from timeit import default_timer as timer


log = Logger("factorize")
LOG_LEVEL = "DEBUG"



class FactorisedNumber(BaseModel):
    factors: list[int] = Field(default=[], description="Prime factors of the number")
    rest: int = Field(description="Left over, used for calculation")
    complex_number: bool = Field(default=True, description="Is the number a complex number or a prime")
    surd: int = 0
    surd_radical_index: int = 2
    value: int = Field(default=None, description="The value of the number with sign")



class FactorizeSmarter:
    def __init__(self):
        self.primes=[]
        self.prime_gen = self.prime_generator()



    def prime_generator(self):
        '''Generates primes, it remember the last prime it generated, and yields once it has found the next one'''
        num = 2
        while True:
            if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
                self.primes.append(num)
                yield (num)
            num += 1

    def highest_common_factor(self, numbers: list):
        # In case we only got one number, lets just return it (the HCF of a single int is itself
        if len(numbers) == 1:
            if isinstance(numbers[0], FactorisedNumber):
                return math.prod(numbers[0].factor)
            return numbers[0]

        # Next lets check that we only received either integers or FactorisedNumbers
        _numbers = []
        for pos in range(0,len(numbers)):
            number = numbers[pos]
            if isinstance(number, FactorisedNumber):
                _numbers.append(number)
            elif isinstance(number, int):
                _numbers.append(self.factoize(number))
            else:
                log.error(f"Unsupported type {type(number)} at postition {pos} in input value {number}")
                raise TypeError(f"Unsupported type {type(number)}")

        # Now lets get counters of the primes in each factorised number and a list of all primes
        prime_counters = [Counter(number.factors) for number in _numbers]

        primes=[number.factors for number in _numbers]
        primes=list(set([num for lst in primes for num in lst]))

        #Lets calculate the HCF by going through the primes, starting on 1 (as all integers are divisible by 1
        hcf = 1
        for prime in primes:
            lowest_number_of_primes = min([ count[prime] for count in prime_counters])
            hcf = hcf * prime ** lowest_number_of_primes


        log.debug(f"We got the prime factors {prime_counters}")
        log.debug(f"And the Highest common factor is {hcf}")
        return hcf

    def lowest_common_multiplier(self, numbers: list):
        # In case we only got one number, lets just return it (the LCM of a single int is itself
        if len(numbers) == 1:
            if isinstance(numbers[0], FactorisedNumber):
                return math.prod(numbers[0].factor)
            return numbers[0]

        # Next lets check that we only received either integers or FactorisedNumbers
        _numbers = []
        for pos in range(0,len(numbers)):
            number = numbers[pos]
            if isinstance(number, FactorisedNumber):
                _numbers.append(number)
            elif isinstance(number, int):
                _numbers.append(self.factoize(number))
            else:
                log.error(f"Unsupported type {type(number)} at postition {pos} in input value {number}")
                raise TypeError(f"Unsupported type {type(number)}")

        # Now lets get counters of the primes in each factorised number and a list of all primes
        prime_counters = [Counter(number.factors) for number in _numbers]

        primes=[number.factors for number in _numbers]
        primes=list(set([num for lst in primes for num in lst]))

        #Lets calculate the LCM by going through the primes, starting on 1
        lcm = 1
        for prime in primes:
            highest_number_of_primes = max([ count[prime] for count in prime_counters])
            lcm = lcm * prime ** highest_number_of_primes


        log.debug(f"We got the prime factors {prime_counters}")
        log.debug(f"Lowest common multiplier is {lcm}")
        return lcm




    def factoize(self, complex_number: int) -> FactorisedNumber:
        response = FactorisedNumber(
            rest=complex_number,
            value= complex_number
        )
        current_prime_possition = -1
        while math.prod(response.factors) != complex_number:
            if current_prime_possition < len(self.primes)-1:
                current_prime_possition += 1
                current_prime = self.primes[current_prime_possition]
            else:
                current_prime = next(self.prime_gen)
                current_prime_possition += 1
                if current_prime_possition > 50:
                    break
            while response.rest % current_prime == 0:
                response.factors.append(current_prime)
                response.rest = response.rest // current_prime



        if complex_number == response.factors[0]:
            response.complex_number = False
        return response



if __name__ == "__main__":
    log = Logger('FACTORIZE')
    log.console.setLevel(LOG_LEVEL)

    fz = FactorizeSmarter()
    fs_first = fz.factoize(180)
    log.info(f"Testing getting Lowest Common Multiplier for {fs_first.value}, 15, 45")
    time = timer()
    lcm = fz.lowest_common_multiplier([fs_first, 15, 45])
    log.info(f"Lowest Common Multiplier (LCM): {lcm} - Took {timer() - time} seconds")

    log.info(f"Testing getting Highest Common Factor for {fs_first.value}, 15, 45")
    time = timer()
    hcf = fz.highest_common_factor([fs_first, 15, 45])
    log.info(f"Highest Common Factor (HCM): {hcf} - Took {timer() - time} seconds")



