# Exercise 12. Computing Simple Interest
# Output:
#   Enter the principal: 1500
#   Enter the rate of interest: 4.3
#   Enter the number of years: 4
#   After 4 years at 4.3%, the investment will be worth $1758.
# Formula:
#   A = P(1 + rt)
#   A: the amount at the end of the investment
#   P: the principal amount
#   r: the annual rate of interest
#   t: the number of years the amount is invested
# Constraints
#   - Prompt for the rate as a percentage (like 15, not .15). Divide the input
#   by 100 in your program.
#   - Ensure that fractions of a cent are rounded up to the next penny.
#   - Ensure that the output is formatted as money.

#!/usr/bin/env python

import sys

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def main():
    try:
        principal = int(input_process('Enter the principal: '))
        interest_rate = float(input_process('Enter the rate of interest: '))
        years = int(input_process('Enter the number of years: '))
    except:
        print('only input number!! bye~')
    else:
        amount = principal*(1 + interest_rate*years/100)
        print_str = 'After {0} years at {1}%, the investment will be worth ${2}.'\
        .format(years, interest_rate, amount)
        print(print_str)

if __name__ == '__main__':
    main()
