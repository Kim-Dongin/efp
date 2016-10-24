# Exercise 10. Self-Checkout
# Output:
#   Price of item 1: 25
#   Quantity of item 1: 2
#   Price of item 2: 10
#   Quantity of item 2: 1
#   Price of item 3: 4
#   Quantity of item 3: 1
#   Subtotal: $64.00
#   Tax: $3.52
#   Total: $67.52
# Constraints:
#   - Keep the input, processing, and output parts of your program seperate.
#   Collect the input, then do the math operation and string building, and then
#   print out the output.
#   - Be sure the explicitly convert input to numerical data before doing any
#   calculations.

#!/usr/bin/env python

import sys

TAX_RATE = 5.5

def input_process(in_str):
    return input(in_str) if (3, 0) <= sys.version_info else raw_input(in_str)

def main():
    item_list = []
    count = 0

    while True:
        try:
            count += 1
            price = int(input_process('Price of item %d: ' % count))
            quantity = int(input_process('Quantity of item %d: ' % count))
            item_list.append((price, quantity))
        except:
            print('only number! bye~')
            break

    subtotal = 0
    for item in item_list:
        subtotal += (item[0] * item[1])

    tax = subtotal * TAX_RATE * 0.01
    total = subtotal + tax

    print_str = '''Subtotal: $%0.2f\nTax: $%0.2f\nTotal: $%0.2f''' \
                % (subtotal, tax, total)
    print(print_str)

if __name__ == '__main__':
    main()
