import random as rd
from num2words import num2words as nw
import number_theory as nt

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

    def __init__(self, num = None, den = None, fraction = None):

        def is_iterable(object):

            try:
                iter_obj = iter(object)
                return True

            except:
                return False


        if num == None and den == None and fraction == None:

            numerator = rd.randint(1, 30)
            denominator = rd.randint(1, 30)

        elif type(num) is int and type(den) is int and fraction == None:

            numerator = num
            denominator = den

        elif num == None and den == None and is_iterable(fraction) and len(fraction) == 2:

            numerator = fraction[0]
            denominator = fraction[1]

        else:

            raise TypeError('Fraction class needs two integers or a list parameter containing two integers')

        self.numerator = numerator
        self.denominator = denominator
        self.fraction = (self.numerator, self.denominator)
        self.name = self.name()
        self.type = self.fraction_type()
        self.latex = u'\u005c' + 'fraction' + "{" + str(self.numerator) + "}" + "{" + str(self.denominator) + "}"


    def name(self):
        '''Names the Fraction object

        Parameters

            self (Fraction class object)

        Returns

            fraction_name (str): the fraction name'''

        numerator_name = nw(self.numerator, lang = 'pt-br').capitalize()

        if str(self.denominator) in FRACTIONAL_NUMBERS_DICT.keys():

            denominator_name = FRACTIONAL_NUMBERS_DICT[str(self.denominator)].lower()

            if self.numerator > 1:

                denominator_name = FRACTIONAL_NUMBERS_DICT[str(self.denominator)] + 's'

        else:

            denominator_name = nw(self.denominator, lang = 'pt-br').lower() + " avos"


        fraction_name  = numerator_name + " " + denominator_name

        return fraction_name


    def fraction_type(self):
        '''Says the type of the Fraction object

        Parameters

            self (Fraction class object)

        Returns

            fraction_type (str): the fraction type'''

        if nt.divisibility(self.denominator, self.numerator):

            fraction_type = 'multiple'

            return fraction_type

        elif self.numerator > self.denominator:

            fraction_type = 'improper'

            return fraction_type

        elif self.numerator < self.denominator:

            fraction_type = 'proper'

            return fraction_type


    def reduce(self):
        '''Gives the reduced fraction of the Fraction object

        Parameters

            self (Fraction class object)

        Returns

            reduced_fraction (Fraction class object): a reduced Fraction Object'''

        k = nt.gcd(self.numerator, self.denominator)

        new_numerator = int(self.numerator / k)

        new_denominator = int(self.denominator / k)

        reduced_fraction = Fraction(fraction = (new_numerator, new_denominator))

        return reduced_fraction


    def invert(self):
        '''Inverts the Fraction object

        Parameters

            self (Fraction class object)

        Returns

            inverted_fraction (Fraction class object): a inverted Fraction Object'''

        inverted_fraction = Fraction(fraction = (self.denominator, self.numerator))

        return inverted_fraction


    def mixed_form(self):

        if self.type == 'proper':

            whole_part = 0
            numerator_part = self.numerator
            denominator_part = self.denominator

            return (whole_part, numerator_part, denominator_part)

        elif self.type == 'improper':

            whole_part = self.numerator // self.denominator
            numerator_part = self.numerator - whole_part * self.denominator
            denominator_part = self.denominator

            return (whole_part, numerator_part, denominator_part)

        elif self.type == 'multiple':

            whole_part = int(self.numerator / self.denominator)
            numerator_part = 0
            denominator_part = 0

            return (whole_part, numerator_part, denominator_part)


def reduce_to_same_denominator(fraction1, fraction2):
    '''Makes the Fraction objects have the same denominator

    Parameters

        fraction1 (Fraction class object): a Fraction object to be reduced to same denominator
        fraction2 (Fraction class object): a Fraction object to be reduced to same denominator

    Returns

        new_fractions (list): a list containing the same-denominator Fraction objects'''

    fractions = [fraction1, fraction2]

    new_fractions = []

    lcm_number = nt.lcm(fraction1.denominator, fraction2.denominator)

    for fraction in fractions:
        
        k = int(lcm_number / fraction.denominator)

        new_fraction = Fraction((fraction.numerator * k, fraction.denominator * k))

        new_fractions.append(new_fraction)

    return new_fractions


def equivalent(fraction1, fraction2):
    '''Tests if the Fraction objects are equivalent

    Parameters

        fraction1 (Fraction class object): a Fraction object to be tested
        fraction2 (Fraction class object): a Fraction object to be tested

    Returns

        result (bool): the logical value that says if the fractions are equivalent or not'''

    if fraction1.reduced == fraction2.reduced:

        result = True

        return result
    
    else:

        result = False

        return result


def compare(fraction1, fraction2):
    '''Compares the Fraction objects to see which one are the greater fraction

    Parameters

        fraction1 (Fraction class object): a Fraction object to be compared
        fraction2 (Fraction class object): a Fraction object to be compared

    Returns

        result_fraction (Fraction class object): the greater Fraction object'''

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
    '''Sums up two Fraction objects

    Parameters

        fraction1 (Fraction class object): a Fraction object to be summed
        fraction2 (Fraction class object): a Fraction object to be summed

    Returns

        result_fraction (Fraction class object): the sum result between both Fraction objects'''

    if fraction1.denominator != fraction2.denominator:

        same_denominator_fractions = reduce_to_same_denominator(fraction1, fraction2)

        fraction1 = same_denominator_fractions[0]
        fraction2 = same_denominator_fractions[1]

    result_fraction = Fraction((fraction1.numerator + fraction2.numerator, fraction1.denominator))

    return result_fraction


def subtract_fractions(fraction1, fraction2):
    '''Subtracts two Fraction objects

    Parameters

        fraction1 (Fraction class object): a Fraction object to be subtracted
        fraction2 (Fraction class object): a Fraction object to be subtracted

    Returns

        result_fraction (Fraction class object): the subtraction result between both Fraction objects'''

    if fraction1.denominator != fraction2.denominator:

        same_denominator_fractions = reduce_to_same_denominator(fraction1, fraction2)

        fraction1 = same_denominator_fractions[0]
        fraction2 = same_denominator_fractions[1]

    result_fraction = Fraction((fraction1.numerator - fraction2.numerator, fraction1.denominator))

    return result_fraction


def multiplie_fractions(fraction1, fraction2):
    '''Multiplies two Fraction objects

    Parameters

        fraction1 (Fraction class object): a Fraction object to be multiplied
        fraction2 (Fraction class object): a Fraction object to be multiplied

    Returns

        result_fraction (Fraction class object): the multiplication result between both Fraction objects'''

    try:

        result_fraction = Fraction((fraction1.numerator * fraction2.numerator, fraction1.denominator * fraction2.denominator))

        return result_fraction

    except:

        result_fraction = Fraction((fraction1 * fraction2.numerator, fraction2.denominator))

        return result_fraction


def divide_fractions(fraction1, fraction2):

    result_fraction = multiplie_fractions(fraction1, fraction2.inverted)
    
    return result_fraction


def power_fraction(fraction, n):
    '''Powers a Fraction object to a exponent

    Parameters

        fraction (Fraction class object): a Fraction object to be powered
        n (int): the exponent for the Fraction object

    Returns

        result_fraction (Fraction class object): the power of the fraction to the n exponent result'''

    if n > 0:

        result_fraction = Fraction((fraction.numerator ** n, fraction.denominator ** n))
    
        return result_fraction

    elif n < 0:

        inverted_fraction = fraction.inverted

        result_fraction = Fraction((inverted_fraction.numerator ** n, inverted_fraction.denominator ** n))

        return result_fraction

    elif n == 0:

        return 1

