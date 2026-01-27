import math
import json
import logging
import sys
from pydantic import BaseModel
from collections import Counter






class FactorisedNumber(BaseModel):
    factors: list[int] = []
    rest: int
    complex_number: bool = True

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
                logging.error(f"Unsupported type {type(number)} at postition {pos} in input value {number}")
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


        logging.debug(f"We got the prime factors {prime_counters}")
        logging.debug(f"And the Highest common factor is {hcf}")
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
                logging.error(f"Unsupported type {type(number)} at postition {pos} in input value {number}")
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


        logging.debug(f"We got the prime factors {prime_counters}")
        logging.debug(f"And the Highest common factor is {lcm}")
        return lcm




    def factoize(self, complex_number: int) -> FactorisedNumber:
        response = FactorisedNumber(
            rest=complex_number
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



        if complex_number != response.factors[0]:
            response.complex_number = False
        return response



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    fz = FactorizeSmarter()
    fs_first = fz.factoize(80)
    fs_second = fz.factoize(54)
    lcm = fz.lowest_common_multiplier([fs_first, 15, 45])

