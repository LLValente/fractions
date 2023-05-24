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

        else:

            self.numerator = fraction[0]
            self.denominator = fraction[1]

        self.fraction = (self.numerator, self.denominator)
        self.reduced = self.reduce()
        self.inverted = self.invert()
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

        if self.numerator > self.denominator:

            fraction_type = 'unwon'

            return fraction_type

        elif self.numerator < self.denominator:

            fraction_type = 'won'

            return fraction_type

        elif divisibility(self.denominator, self.numerator):

            fraction_type = 'multiple'

            return fraction_type


    def reduce(self):

        k = nb.gcd(self.numerator, self.denominator)

        new_numerator = int(self.numerator / k)

        new_denominator = int(self.denominator / k)

        reduced_fraction = Fraction((new_numerator, new_denominator))

        return reduced_fraction

    def invert(self):

        inverted_fraction = Fraction((self.denominator, self.numerator))

        return inverted_fraction


def reduce_to_same_denominator(fraction1, fraction2):

    fractions = [fraction1, fraction2]

    new_fractions = []

    lcm_number = nb.lcm(fraction1.denominator, fraction2.denominator)

    for fraction in fractions:
        
        k = int(lcm_number / fraction.denominator)

        new_fraction = Fraction((fraction.numerator * k, fraction.denominator * k))

        new_fractions.append(new_fraction)

    return new_fractions


def equivalent(fraction1, fraction2):

    if fraction1.reduced == fraction2.reduced:

        result = True

        return result
    
    else:

        result = False

        return result


def compare(fraction1, fraction2):

    if fraction1.denominator != fraction2.denominator:

        same_denominator_fractions = reduce_to_same_denominator(fraction1, fraction2)

        fraction1 = same_denominator_fractions[0]
        fraction2 = same_denominator_fractions[1]

    if fraction1.numerator > fraction2.numerator:

        result_fraction = fraction1

        return result_fraction

    elif fraction1.numerator < fraction2.numerator:

        result_fraction = fraction2

        return result_fraction
    
    else:

        return "As frações são equivalentes"


def sum_fractions(fraction1, fraction2):

    if fraction1.denominator != fraction2.denominator:

        same_denominator_fractions = reduce_to_same_denominator(fraction1, fraction2)

        fraction1 = same_denominator_fractions[0]
        fraction2 = same_denominator_fractions[1]

    result_fraction = Fraction((fraction1.numerator + fraction2.numerator, fraction1.denominator))

    return result_fraction


def subtract_fractions(fraction1, fraction2):

    if fraction1.denominator != fraction2.denominator:

        same_denominator_fractions = reduce_to_same_denominator(fraction1, fraction2)

        fraction1 = same_denominator_fractions[0]
        fraction2 = same_denominator_fractions[1]

    result_fraction = Fraction((fraction1.numerator - fraction2.numerator, fraction1.denominator))

    return result_fraction


def multiplie_fractions(fraction1, fraction2):

    try:

        result_fraction = Fraction((fraction1.numerator * fraction2.numerator, fraction1.denominator * fraction2.denominator))

        return result_fraction

    except:

        result_fraction = Fraction((fraction1 * fraction2.numerator, fraction2.denominator))

        return result_fraction


def power_fraction(fraction, exponent):

    result_fraction = Fraction((fraction.numerator ** exponent, fraction.denominator ** exponent))

    return result_fraction