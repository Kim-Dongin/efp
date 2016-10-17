# Exercise 6. Retirement Calculator
# Output:
#   What is your current age? 25
#   At what age would you like to retire? 65
#   You have 40 years left until you can retire.
#   It's 2015, so you can retire in 2055.
# Constraints:
#   - Again, be sure to convert the input to numerical data before doing any
#   math.
#   - Don't hard-code the current year into your program. Get it from the
#   system time via your programming language.


#!/usr/bin/env python

import sys
import time

def input_process(in_input):
    return input(in_input) if (3,0) <= sys.version_info else raw_input(in_input)

def main():
    try:
        current_age = int(input_process('What is your current age? '))
        retiring_age = int(input_process('At what age would you like to retire? '))
    except:
        print('Enter the only number!!! bye~')
    else:
        left_retire = int(retiring_age - current_age)

        if left_retire < 0:
            print('Wrong retiring_age.')
            exit(1)

        left_retire_str = 'You have %d years left until you can retire.' % left_retire
        print(left_retire_str)

        current_year = int(time.strftime('%Y', time.localtime(time.time())))
        retiring_year = current_year + left_retire

        print_str = 'It\'s %d, so you can retire in %d' % (current_year, retiring_year)
        print(print_str)

if __name__ == '__main__':
    main()
