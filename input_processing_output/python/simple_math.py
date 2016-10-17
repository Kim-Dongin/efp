# Exercise 5. Simple Math
# Output:
#   What is the first number? 10
#   What is the second number? 5
#   10 + 5 = 15
#   10 - 5 = 5
#   10 * 5 = 50
#   10 / 5 = 2
# Contraints:
#   - Values coming from users will be string. Ensure that you convert these
#   values to numbers before doing the math.
#   - Keep the inputs and outputs seperate from the numerical conversion and
#   other processing
#   - Generate a single output statement with line breaks in the appropriate
#   spots.


#!/usr/bin/env pythone

import sys

def input_process(in_input):
    return input(in_input) if (3,0) <= sys.version_info else raw_input(in_input)

def plus(in_first, in_second):
    return int(in_first + in_second)

def minus(in_first, in_second):
    return int(in_first - in_second)

def mutiply(in_first, in_second):
    return int(in_first * in_second)

def division(in_first, in_second):
    return int(in_first / in_second)

def main():
    first_num_str = input_process('What is the first number? ')
    second_num_str = input_process('What is the second number? ')

    try:
        first_num = int(first_num_str)
        second_num = int(second_num_str)
    except:
        print('Enter the number!!BYE~')
    else:
        plus_num = plus(first_num, second_num)
        minus_num = minus(first_num, second_num)
        multi_num = mutiply(first_num, second_num)
        division_num = division(first_num, second_num)

        print_str = '%d + %d = %d\n' % (first_num, second_num, plus_num)
        print_str += '%d - %d = %d\n' % (first_num, second_num, minus_num)
        print_str += '%d * %d = %d\n' % (first_num, second_num, multi_num)
        print_str += '%d / %d = %d' % (first_num, second_num, division_num)

        print(print_str)


if __name__ == '__main__':
    main()
