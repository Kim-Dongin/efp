# Exercise 9. Paint Calculator
# Output:
#   You will need to purchase 2 gallons of paint to cover 360 square feet.
# Constraints:
#   - Use a constant to hold the conversion rate.
#   - Ensure that you round up to the next whole number.

#!/usr/bin/env python

import sys
import math

def input_process(in_string):
    return input(in_string) if (3, 0) <= sys.version_info else raw_input(in_string)

def main():
    try:
        length = int(input_process('What is the length of the room in feet? '))
        width = int(input_process('What is the width of the room in feet? '))
    except:
        print('Only Enter the number!!! bye~~')
    else:
        square_feet= length * width
        cover_feet = 350
        gallons = math.ceil(square_feet / (cover_feet * 1.0))
        print_string = 'You will need to purchase %d gallons of paint to '\
                        'cover %d square feet.' % (gallons, square_feet)
        print(print_string)

if __name__ == '__main__':
    main()
