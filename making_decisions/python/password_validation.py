# Exercise 15. Password Validation
# Output:
#   What is the password? 12345
#   I don't know you.
#   or
#   What is the password? abc$123
#   Welcome!
# Constraints:
#   - Use an if/else statement for this program.
#   - Make sure the program is case sensitive.

#!/usr/bin/env python

import sys

ID = 'dongin'
PASSWD = 'abc$123'
INCORRECT = 'I don\' know you.'
CORRECT = 'Welcome!'

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def validate_passwd(in_name, in_passwd):
    if(in_name == ID) & (in_passwd == PASSWD):
        return True
    return False

def main():
    user_name = input_process('What is the id: ')
    user_passwd = input_process('What is the password: ')
    result = validate_passwd(user_name, user_passwd)
    if result is True:
        print(CORRECT)
    else:
        print(INCORRECT)
    return True

if __name__ == '__main__':
    main()
