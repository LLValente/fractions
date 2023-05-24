import random as rd
from num2words import num2words as nw

FRACTIONAL_NUMBERS_DICT =   {"2": "meio",
                    "3": "terço",
                    "4": 'quarto',
                    "5": 'quinto',
                    "6": 'sexto',
                    "7": 'sétimo',
                    "8": 'oitavo',
                    "9": 'nono',
                    "10": 'décimo',
                    "100": 'centésimo'}         

QUESTIONS_START =   {'': '', 
                    '': '', 
                    '': '', 
                    '': ''}

QUESTIONS_END =     {'': '', 
                    '': '', 
                    '': '', 
                    '': ''}       

class Fracao:

    def __init__(self, fraction=()):

        if fraction == ():

            self.numerator = rd.randint(1, 1000)
            self.denominator = rd.randint(1, 1000)
            self.fraction = (self.numerator, self.denominator)

        else:

            self.numerator = fraction[0]
            self.denominator = fraction[1]
            self.fraction = (fraction[0], fraction[1])

        self.reduced = self.reduce()
        self.name = self.name()
        self.type = self.fraction_type()
        self.latex = u'\u005c' + 'fraction' + "{" + str(self.numerator) + "}" + "{" + str(self.denominator) + "}"


    def name(self):

        numerator_name = nw(self.numerator, lang = 'pt-br').capitalize()

        if str(self.denominator) in FRACTIONAL_NUMBERS_DICT.keys():

            denominator_name = FRACTIONAL_NUMBERS_DICT[str(self.denominator)].lower()

            if self.numerator > 1:

                denominator_name = str(self.denominator) + 's'

        else:

            denominator_name = nw(self.denominator, lang = 'pt-br').lower() + " avos"


        fraction_name  = numerator_name + " " + denominator_name

        return fraction_name


    def fraction_type(self):

        if divisibility(self.denominator, self.numerator):

            return 'multiple'

        elif self.numerator > self.denominator:

            return 'unwon'

        elif self.numerator < self.denominator:

            return 'own'


    def reduce(self):

        k = gcd(self.fraction[0], self.fraction[1])

        numerator = int(self.fraction[0]/k)

        denominator = int(self.fraction[1]/k)

        reduced_fraction = (numerator, denominator)

        return reduced_fraction

    
class Question:

    def __init__(self):

        #self.start = QUESTIONS_START[self.type]
        #self.end = QUESTIONS_START[self.type]
        self.items = self.items()
        self.answears = ''

    def items(self, items_numbers = 6):

        fractions = []

        i = 1

        while i <= items_numbers:

            fraction = Fracao()
            fractions.append(fraction)

            i += 1

        return fractions


def divisibility(num1, num2):

    if num2 % num1 == 0:

        return True

    else:

        return False 


def divisors(number):

    divisors = []

    for i in range(1, number + 1):

        if divisibility(i, number):

            divisors.append(i)

    return divisors


def prime(number):

    divisors_numbers = divisors(number)

    if len(divisors_numbers) == 2 and 1 in divisors_numbers and number in divisors_numbers:

        return True

    else: 

        return False


def prime_numbers_until(number):

    prime_numbers = []

    i = 1

    while i <= number:

        if prime(i):

            prime_numbers.append(i)

        i += 1

    return prime_numbers


def gcd(num1, num2):

    max_number = max(num1, num2)
    min_number = min(num1, num2)

    max_number_divisors = divisors(max_number)
    min_number_divisors = divisors(min_number)

    intersection = []

    for number in max_number_divisors:

        if number in min_number_divisors:

            intersection.append(number)

    gcd = max(intersection)

    return gcd

    
def lcm(num1, num2):

        max_number = max(num1, num2)
        min_number = min(num1, num2)

        primes = prime_numbers_until(max_number)

        col1 = num1
        col2 = num2

        lcm_number = 1

        while True:

            for prime in primes:

                prime_divides_col1 = divisibility(prime, col1)
                prime_divides_col2 = divisibility(prime, col2)

                if prime_divides_col1 and prime_divides_col2:

                    col1 = int(col1 / prime)
                    col2 = int(col2 / prime)

                    lcm_number = lcm_number * prime

                    break

                elif prime_divides_col1:

                    col1 = int(col1 / prime)

                    lcm_number = lcm_number * prime

                    break

                elif prime_divides_col2:

                    col2 = int(col2 / prime)

                    lcm_number = lcm_number * prime

                    break

            if col1 == 1 and col2 ==1:

                break
        
        return lcm_number


def denominator_reduction(fraction1, fraction2):

    lcm_number = lcm(fraction1.denominator, fraction2.denominator)

    for num in [1, 2]:
        
        k = int(lcm_number / eval(f'fraction{num}').denominator)

        eval(f'fraction{num}').numerator = eval(f'fraction{num}').numerator * k
        eval(f'fraction{num}').denominator = eval(f'fraction{num}').denominator * k

    return (Fracao(fraction1.fraction), Fracao(fraction2.fraction))


def equivalent(fraction1, fraction2):

    if fraction1.reduced == fraction2.reduced:

        return True
    
    else:

        return False


def compare(fraction1, fraction2):

    if fraction1.denominator != fraction2.denominator:

        fraction1, fraction2 = denominator_reduction(fraction1, fraction2)

        if fraction1[0]

    else:
    
        (fraction1, fraction2)

question1 = Question()
print(question1.items)