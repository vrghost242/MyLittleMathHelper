import math
import json
NUMBER_OF_PRIMES = 3

class factorizer:
    def __init__(self):
        self.primes = []
        self.prime_gen = self.prime_generator()
        while len(self.primes) < NUMBER_OF_PRIMES:
            # Lets start by generating the firls set of primes
            self.primes.append(next(self.prime_gen))

    def prime_generator(self):
        for num in range(2, 2000000):
            if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
                yield(num)

    def is_factor(self, numerator: int, denominator: int):
        return numerator % denominator == 0
    def factoize(self, complex_number: int):
        print(f"Factorizing {complex_number}")
        response = {
            "factors": [],
            "rest": complex_number,
            "complex_number": True
        }
        while math.prod(response["factors"]) != complex_number:
            for prime in self.primes:
                if self.is_factor(response["rest"], prime):
                    response["factors"].append(prime)
                    print(f"For {complex_number} Found prime factor {prime} on rest {response['rest']}")
                    response["rest"] = response["rest"] // prime
                    if math.prod(response["factors"]) == complex_number:
                        print(f"For {complex_number} Found factors {response['factors']}")
                        break


            if response["rest"] != 1:

                next_prime = next(self.prime_gen)
                print(f"No prime factors found, checking for next prime {next_prime}")
                self.primes.append(next_prime)
                if  self.is_factor(response["rest"], next_prime):
                    response["factors"].append(next_prime)
                    response["rest"] = response["rest"] // next_prime
            if len(response["factors"]) == 1:
                response["complex_number"] = False

        return response




if __name__ == '__main__':
    fz = factorizer()
    factored_number = fz.factoize(3)
    print(json.dumps(factored_number, indent=4))
    factored_number = fz.factoize(17)
    print(json.dumps(factored_number, indent=4))
    factored_number = fz.factoize(15)
    print(json.dumps(factored_number, indent=4))
    factored_number = fz.factoize(67)
    print(json.dumps(factored_number, indent=4))
    factored_number = fz.factoize(167)
    print(json.dumps(factored_number, indent=4))
    factored_number = fz.factoize(166)
    print(json.dumps(factored_number, indent=4))
    factored_number = fz.factoize(160)
    print(json.dumps(factored_number, indent=4))