import random as rd
from fractions import Fraction

class Periodic_decimal:

    def __init__(self, num_integers = 1, num_non_periodical_numbers = 0, num_periodical_numbers = 1):

        def generate_periodic_decimal(num_integers, num_non_periodical_numbers, num_periodical_numbers):
            '''Creates a periodic decimal 
            
            Parameters:
            num_integers (int): number of intergers before comma
            num_non_periodical_numbers (int): number of non-periodical intergers after comma
            num_periodical_numbers (int): number of periodical intergers after comma

            Returns:
            str: returns a decimal number with ellipsis notation'''

            if num_integers == 0:
                
                integer_part = str(0)

            else:

                integer_lower_limit = "1" + "0" * (num_integers - 1)
                integer_upper_limit = "9" * num_integers

                integer_part = str(rd.randint(int(integer_lower_limit), int(integer_upper_limit)))
                
            periodic_decimal = integer_part + ","

            periodic_lower_limit = "1" + "0" * (num_periodical_numbers - 1)
            periodic_upper_limit = "9" * num_periodical_numbers

            periodic_part = str(rd.randint(int(periodic_lower_limit), int(periodic_upper_limit)))

            non_periodical_number_after_comma = ""

            for i in range(0, num_non_periodical_numbers):

                to_be_added_after_comma_number = str(rd.randint(0, 9))

                non_periodical_number_after_comma = non_periodical_number_after_comma + to_be_added_after_comma_number

            periodic_decimal = periodic_decimal + non_periodical_number_after_comma

            for i in range(0, 3):

                periodic_decimal = periodic_decimal + periodic_part

            periodic_decimal = periodic_decimal + "..."          

            return periodic_decimal


        def periodic_type(self):

            if num_non_periodical_numbers == 0:

                periodic_type = 'simple'

            elif num_non_periodical_numbers != 0:

                periodic_type = 'complex'

            return periodic_type


        def original_fraction(self):

            if self.type == 'simple':

                if num_integers == 0:

                    integer_part = self.periodic[0]

                else:

                    integer_part = self.periodic[:num_integers]

                period = self.periodic[-num_periodical_numbers-3:-3]

                numerator = int(integer_part + period) - int(integer_part)

                denominator = int('9' * num_periodical_numbers)

                return (numerator, denominator)

            elif self.type == 'complex':

                if num_integers == 0:

                    integer_part = self.periodic[0]

                else:

                    integer_part = self.periodic[:num_integers]

                antiperiod = self.periodic[num_integers + 1:num_integers + 1 + num_non_periodical_numbers]

                period = self.periodic[-num_periodical_numbers-3:-3]

                numerator = int(integer_part + antiperiod + period) - int(integer_part + antiperiod)

                denominator = int('9' * num_periodical_numbers + '0' * len(antiperiod))

                return (numerator, denominator)
            
        self.periodic = generate_periodic_decimal(num_integers, num_non_periodical_numbers, num_periodical_numbers)

        self.type = periodic_type(self)

        self.original_fraction = original_fraction(self)

