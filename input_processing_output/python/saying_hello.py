# Practice 1. Saying Hello
# Output:
#   What is your name? Brian
#   Hello, Brian, nice to meet you!
# Constraint:
#   Keep the input, string concatenation, and output separate.


#!/usr/bin/env python

import sys

def input_process(in_name):
    return input(in_name) if (3,0) <= sys.version_info else raw_input(in_name)

def main():
    try:
        name = str(input_process('What is your name? '))
        hello = 'Hello, ' + name + ', nice to meet you!'
        print(hello)
    except:
        print('Please input your name.')

if __name__ == '__main__':
    main()
