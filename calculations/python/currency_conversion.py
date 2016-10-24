# Exercise 11. Currency conversion
# ammount_to = (ammount_from * rate_from) / rate_to
# Output:
#   How many euros are you exchanging? 81
#   What is the exchange rate? 137.51
#   81 euros at an exchange rate of 137.51 is 111.38 U.S. dollars.
# Constraints:
#   - Enxure that fractions of a cent are rounded up the next penny.
#   - Use a single output statement.

#!/usr/bin/env python

import sys
import math

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def main():
    try:
        euros = float(input_process('How many euros are you exchanging? '))
        exchange_rate = float(input_process('What is the exchange rate? '))
    except:
        print('only input number!!! bye~~')
    else:
        dollars = euros * exchange_rate / 100
        #if ((dollars * 1000) % 10 > 0 ): dollars += 0.01
        print_str = '%d euros at an exchange rate of %0.2f is %0.2f U.S. dollars' \
                    % (euros, exchange_rate, dollars)
        print(print_str)

if __name__ == '__main__':
    main()
