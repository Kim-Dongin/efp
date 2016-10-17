# Exercise 4. Mad Lib
# Output:
#   Enter a noun: dog
#   Enter a verb: walk
#   Enter an adjective: blue
#   Enter an adverb: quickly
#   Do you walk your blue dog quickly? That's hilarious!
# Constraints:
#   - Use a single output statement for this program.
#   - If your language supports string interpolation or string substitution,
#   use it to build up the output.


#!/usr/bin/env pythone

import sys

def input_process(in_input):
    return input(in_input) if (3,0) <= sys.version_info else raw_input(in_input)

def main():
    noun = str(input_process('Enter a noun: '))
    verb = str(input_process('Enter a verb: '))
    adjective = str(input_process('Enter an adjective: '))
    adverb = str(input_process('Enter an adverb: '))

    mad_str = 'Do you %s your %s %s %s? That\'s hilarous!' % (verb, noun, adjective, adverb)
    print(mad_str)

if __name__ == '__main__':
    main()
