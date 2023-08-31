class DifficultyOne:

    # Given a number n, check whether n is prime.
    # https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

    # Remember, a number is prime if it has no divisors.

    # You can use the % operator to see the remainder of a division.
    # Examples:
    # 10 % 2 evaluates to 0
    # 10 % 3 evaluates to 1
    # 10 % 4 evaluates to 2
    # n % x evaluates to 0 if n is divisible by x

    # The following example shows how you would write a function to check
    # whether n is even

    # def check_is_even(self, n):
    #     return n % 2 == 0

    # finish implementing the check prime function.
    # this is partially implemented, but contains one todo item.
    # other comments are just explanation and do not require modification.

    def check_if_prime(self, n):
        # iterate over each number less than n and greater than 1
        for x in range(2, n):
            if True: # <- todo replace "True" with a condition to check whether x divides n
                return False
        # return True at the end because if the code has reached this point without
        # returning False, then nothing divides n
        return True

    # Return a list containing the overlap between two other lists
    # https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

    # Example:
    # Given
    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # your function should return
    # [1, 2, 3, 5, 8, 13]

    # Python list comprehensions would be appropriate for this problem,
    # but for now, we will implement this with normal loops and conditions.

    # this is partially implemented, but contains mostly psuedocode to be
    # implemented.

    def find_overlap(self, a, b):
        # "out" defines our output list. It is initialized as an empty list.
        out = []
        # todo: iterate over a with iterator x
        # todo: with a nested loop, iterate over b with iterator y
        # todo: inside of the inner loop, check whether x and y are equal
        # todo: inside of the 'if' body, add x or y, which are the same, to out
        # "out", now populated, is returned.
        return out

    # Implement "cows and bulls"
    # https://www.practicepython.org/solution/2014/07/18/18-cows-and-bulls-solutions.html

    # Unlike on the website, your function does not need to run in a loop and repeatedly take
    # user input. Instead, use a hard-coded number (provided) to compare with the function
    # parameter "x".

    # "x" will be a four-digit number like the provided number in your function. For each digit
    # that x has that matches the corresponding digit in "number", that is a "cow". For each digit
    # that x has in common with "number" that is not in the correct position, that is a "bull".
    # Return the number of cows and bulls in an array like this:

    # [0, 0]

    # Remember to cast your numbers as strings with the str(x) function to do string comparisons!

    def cows_and_bulls(self, x):
        # provided arbitrary number
        number = 3721
        # "cows" count
        cows = 0
        # "bulls" count
        bulls = 0
        for i in range(len(str(x))):
            pass # todo <- Delete this upon implementing
            # todo check whether the character at position "i" in str(x) is the same as the character
            # todo ...at position "i" in str(number).
            # todo If so, add 1 to cows. Else, continue to check for bulls
            # todo To check for a bull, get the character at position "i" in str(x), then use
            # todo ..."<character> in str(number)" to see if "number" contains that digit
        return [cows, bulls]