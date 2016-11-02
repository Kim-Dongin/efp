# Exercise 16. Legal Driving Age
# Output:
#   What is your age? 15
#   You are not old enough to legally drive.
#   or
#   What is your age? 35
#   You are old enough to legally drive.
# Constraints:
#   - Use a single output statement.
#   - Use a ternary operator to write this program. If your language doesn’t
#   support a ternary operator, use a reg- ular if/else statement, and still
#   use a single output state- ment to display the message.

#!/usr/bin/env python

import sys

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def main():
    return True

if __name__ == '__main__':
    main()
