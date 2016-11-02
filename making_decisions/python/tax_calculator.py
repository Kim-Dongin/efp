# Exercise 14. Tax Calculator
# Output:
#   What is the order amount? 10
#   What is the state? WI
#   The subtotal is $10.00.
#   The tax is $0.55.
#   The total is $10.55.
#   ...
#   What is the order amount? 10
#   What is the state? MN
#   The total is $10.00
# Constraints:
#   - Implements this program using only simple if statement - don't use an
#   else clause.
#   - Ensure that all money is rounded up to the nearest cent.
#   - Use a single output statement at the end of the program to display the
#   program results.

#!/usr/bin/env python

import sys

WISCONSIN = 'WI'
TAX = 5.5

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def main():
    try:
        amount = int(input_process('What is the order amount? '))
        state = input_process('What is the state? ')
    except:
        print('amount must be number. bye~~')
    else:
        amount_tax = 0
        print_str = ''
        if state.upper() == WISCONSIN:
            amount_tax = amount * (TAX / 100)
            print_str += 'The subtotal is $%d.\n' % amount
            print_str += 'The tax is $%0.2f.\n' % amount_tax

        total = amount + amount_tax
        print_str += 'The total is $%0.2f.' % total
        print(print_str)

if __name__ == '__main__':
    main()
