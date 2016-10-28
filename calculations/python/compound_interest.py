# Exercise 13. Determing Compound Interest
# Output:
# Formula:
#   A = P(1 + r/n) nt
#   P is the principal amount.
#   r is the annual rate of interest.
#   t is the number of years the amount is invested.
#   n isthenumberoftimestheinterestiscompoundedper year.
#   A is the amount at the end of the investment.
# Output:
#   What is the principal amount? 1500
#   What is the rate? 4.3
#   What is the number of years? 6
#   What is the number of times the interest is compounded per year? 4
#   $1500 invested at 4.3% for 6 years compounded 4 times per year is $1938.84.
# Constraints:
#   - Prompt for the rate as a percentage (like 15, not .15). Divide the input
#   by 100 in your program.
#   - Ensure that fractions of a cent are rounded up to the next penny.
#   - Ensure that the output is formatted as money.

#! /usr/bin/env python

import sys
import math

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def main():
    try:
        principal_amount = int(input_process('What is the principal amount? '))
        interest_rate = float(input_process('What is the rate? '))
        years = int(input_process('What is the number of years? '))
        times = int(input_process('What is the number of times the interest is compounded per year? '))
    except:
        print('only input number!! bye~')
    else:
        investment_amount = principal_amount*((1 + interest_rate/(times*100))**(times*years))
        investment_amount = math.ceil(investment_amount * 100) / 100
        print_str = '{0} invested at {1}% for {2} years compounded {3} times per year is {4:0.2f}'\
                    .format(principal_amount, interest_rate, years, times, investment_amount)
        print(print_str)


if __name__ == '__main__':
    main()
