# Exercise 16. Legal Driving Age
# Output:
#   What is your age? 15
#   You are not old enough to legally drive.
#   or
#   What is your age? 35
#   You are old enough to legally drive.
# Constraints:
#   - Use a single output statement.
#   - Use a ternary operator to write this program. If your language does not
#   support a ternary operator, use a regular if/else statement, and still
#   use a single output state- ment to display the message.

#!/usr/bin/env python

import sys

LEGAL_DRIVING_AGE = 16
ILLEGAL_MSG = 'You are not old enough to legally drive.'
LEGAL_MSG = 'You are old enough to legally drive.'

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def print_msg(in_str):
    print(in_str)

def main():
    try:
        age = int(input_process('What is your age? '))
    except:
        print('Age must be number. bye~')
    else:
        print_msg(ILLEGAL_MSG) if age < LEGAL_DRIVING_AGE else print_msg(LEGAL_MSG)

    return True

if __name__ == '__main__':
    main()
