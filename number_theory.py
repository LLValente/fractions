def divisibility(num1, num2):
    '''Tests if a number divides another number

        Parameters

        num1 (int): the divisor number
        num2 (int): the number to divided 

        Returns

        gcd_number (int): the greatest commom divisor between num1 and num2'''

    if num2 % num1 == 0:

        logical_result = True


        return logical_result

    else:

        logical_result = False

        return logical_result


def divisors(number):
    '''Gives a list of divisors of a number

        Parameters

        number (int)

        Returns

        logical_result (bool)'''

    divisors = []

    for i in range(1, number + 1):

        if divisibility(i, number):

            divisors.append(i)

    return divisors


def prime(number):
    '''Tests if a number is either prime or not prime

        Parameters

        number (int): number to be tested

        Returns

        logical_result (bool)'''


    divisors_numbers = divisors(number)

    if len(divisors_numbers) == 2 and 1 in divisors_numbers and number in divisors_numbers:

        logical_result = True

        return logical_result

    else: 

        logical_result = False

        return logical_result


def prime_numbers_until(number):
    '''Returns a list of prime numbers lesser or equal to number variable

        Parameters

        number (int): upper limit of the list

        Returns

        prime_numbers (list): a list containing prime numbers lesser or equal to number variable'''

    prime_numbers = []

    i = 1

    while i <= number:

        if prime(i):

            prime_numbers.append(i)

        i += 1

    return prime_numbers


def gcd(num1, num2):
    '''Returns the greatest commom divisor between two numbers

        Parameters

        num1 (int): a number to be calculated gcd with
        num2 (int): a number to be calculated gcd with

        Returns

        gcd_number (int): the greatest commom divisor between num1 and num2'''

    max_number = max(num1, num2)
    min_number = min(num1, num2)

    max_number_divisors = divisors(max_number)
    min_number_divisors = divisors(min_number)

    intersection = []

    for number in max_number_divisors:

        if number in min_number_divisors:

            intersection.append(number)

    gcd_number = max(intersection)

    return gcd_number

    
def lcm(num1, num2):
    '''Returns the least commom multiple between two numbers

        Parameters

        num1 (int): a number to be calculated lcm with
        num2 (int): a number to be calculated lcm with

        Returns

        lcm_number (int): the least commom multiple between num1 and num2'''

    k = 1

    mult_num1 = num1 * k
    mult_num2 = num2 * k

    while mult_num1 != mult_num2:

        k += 1

        mult_num1 = num1 * k
        mult_num2 = num2 * k

    lcm_number = mult_num1

    return lcm_number

