# Exercise 7. Area of a Rectangular Room
# Output:
#   What is the length of the room in feet? 15
#   What is the width of the room in feet? 20
#   You entered dimensions of 15 feet by 20 feet.
#   The area is
#   300 square feet
#   27.871 square meters
# Constraints:
#   - Keep the calculations seperate from the output.
#   - Use a constant to hold the conversion factor.

#!/usr/bin/env python

import sys
import math

NUM = 0.09290304

def input_process(in_string):
    return input(in_string) if (3, 0) <= sys.version_info else raw_input(in_string)

def feet_to_meters(in_number):
    return float(math.sqrt(in_number**2 * NUM))

def main():
    try:
        length = int(input_process('What is the length of the room in feet? '))
        width = int(input_process('What is the width of the room in feet? '))
    except:
        print('Only Enter the number!!! bye~~')
    else:
        print('You entered dimensions of %d feet by %d feet.') % (length, width)
        area_of_feet = length * width
        area_of_meters = feet_to_meters(area_of_feet)
        print_string = 'The area is\n'
        print_string += '%d square feet\n' % area_of_feet
        print_string += '%f square meters' % area_of_meters
        print(print_string)

if __name__ == '__main__':
    main()
