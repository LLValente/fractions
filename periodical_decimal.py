class periodic_decimal:

    def __init__(self, type='simple'):

        if type == 'simple':

            self.periodic = generate_simple_periodic_decimal()

        elif type == 'complex':

            self.periodic = generate_complex_periodic_decimal()

        self.fraction = original_fraction()

        pass

    def generate_simple_periodic_decimal(num_integers = 1, num_periodical_numbers = 1):
        '''Create a simple periodic decimal 
        
        Parameters:
        num_integers (int): number of intergers before comma
        num_periodical_numbers (int): number of periodical intergers after comma

        Returns:
        str: returns a decimal number with ellipsis notation'''

        integer_upper_limit = "9" * num_integers

        integer_lower_limit = "1" + "0" * (num_integers - 1)

        integer_part = str(rd.randint(int(integer_lower_limit), int(integer_upper_limit)))

        periodic_decimal = integer_part + ","

        periodic_upper_limit = "9" * num_periodical_numbers

        periodic_lower_limit = "1" + "0" * (num_periodical_numbers - 1)

        periodical_part = str(rd.randint(int(periodic_lower_limit), int(periodic_upper_limit)))

        for i in range(0, 3):

            periodic_decimal = periodic_decimal + periodical_part

        periodic_decimal = periodic_decimal + "..."

        return periodic_decimal


    def generate_complex_periodic_decimal(num_integers = 1, num_non_periodical_numbers = 2, num_periodical_numbers = 1):
        '''Create a complex periodic decimal 
        
        Parameters:
        num_integers (int): number of intergers before comma
        num_non_periodical_numbers (int): number of non-periodical intergers after comma
        num_periodical_numbers (int): number of periodical intergers after comma

        Returns:
        str: returns a decimal number with ellipsis notation'''

        integer_upper_limit = "9" * num_integers

        integer_lower_limit = "1" + "0" * (num_integers - 1)

        integer_part = str(rd.randint(int(integer_lower_limit), int(integer_upper_limit)))

        periodic_decimal = integer_part + ","

        periodic_upper_limit = "9" * num_periodical_numbers

        periodic_lower_limit = "1" + "0" * (num_periodical_numbers - 1)

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


    def original_fraction(self):

        periodic_decimal = self.periodic

        

        pass

