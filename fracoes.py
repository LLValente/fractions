import random as rd
from num2words import num2words as nw
import numbers as nb

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


class Fraction:

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

        k = nb.gcd(self.fraction[0], self.fraction[1])

        numerator = int(self.fraction[0]/k)

        denominator = int(self.fraction[1]/k)

        reduced_fraction = Fraction((numerator, denominator))

        return reduced_fraction


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