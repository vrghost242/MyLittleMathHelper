import math
import json
from pydantic import BaseModel

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


    def higest_common_factor(self, first: FactorisedNumber, second: FactorisedNumber):
    def factoize(self, complex_number: int) -> FactorisedNumber:
        response = FactorisedNumber(
            rest=complex_number
        )
        last_known_prime = self.primes[-1]
        current_prime_possition = -1
        current_prime = self.primes[current_prime_possition]
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
    fz = FactorizeSmarter()
    for i in range(20):
        next(fz.prime_gen)
    print(fz.primes)
    for i in [17 , 167, 166, 160, 15, 3600]:
        print(f"Factorising {i}")
        print(json.dumps(fz.factoize(i).model_dump(), indent=4))

