# Exercise 8. Pizza Party
# Output:
#   How many people? 8
#   How many pizzas do you have? 2
#   8 people with 2 pizzas
#   Each person gets 2 pieces of pizza.
#   How many pieces are in a pizza? 8
#   There are 0 leftover pieces.

#!/usr/bin/env python

import sys

def input_process(in_string):
    return input(in_string) if (3, 0) <= sys.version_info else raw_input(in_string)

def main():
    try:
        people_num = int(input_process('How many people? '))
        pizza_num = int(input_process('How many pizzas do you have? '))
        pieces_num = int(input_process('How many pieces are in a pizza? '))
    except:
        print('only Enter the number!!! bye~')
    else:
        if (pieces_num % 2 == 1):
            print('Pieces number should be even number.')
            exit(0)
        total_pieces = pizza_num * pieces_num
        print('%d people with %d pizzas') % (people_num, pizza_num)
        print('Each person gets %d pieces of pizza.') % (total_pieces / people_num)
        print('There are %d leftover pieces.') % (total_pieces % people_num)

if __name__ == '__main__':
    main()
