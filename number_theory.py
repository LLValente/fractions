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

