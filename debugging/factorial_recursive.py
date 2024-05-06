#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    - n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    - int: The factorial of the input integer.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: calculate factorial using recursion
        return n * factorial(n-1)


# Get the factorial of the number provided as a command-line argument
f = factorial(int(sys.argv[1]))
# Print the factorial
print(f)
