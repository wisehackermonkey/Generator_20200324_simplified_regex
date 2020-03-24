#Simplified regex text generator 
#20200324
#by oran collins

import random
import string
# import filter

import re # for regex

# random uppercase random.choice(string.ascii_letters)
# ascii_letters, ascii_uppercase, and ascii_lowercase





def char_range_gen(start="", end=""):
    # if start != "" and end != "":

    start_range = ord(start)
    # the plus +1 makes the range include the end value in the random selection of letters
    stop_range =  ord(start) + (ord(end) - ord(start) )+1 
    return chr(random.randrange(start_range, stop_range) )


def int_range_gen(start=0, end=0):
    return random.randrange(start,end + 1)


def parse_controll_characters(string):
    parsed_string = re.split(r'[-\[\]\s]\s*', string)

    removed_empties = list(filter(None, parsed_string))
    return removed_empties
    


def parse_letters(string):
    removed_empties = parse_controll_characters(string)
    
    start_range = removed_empties[0]
    end_range = removed_empties[1]
    
    return char_range_gen(start=start_range,end=end_range)


def parse_numbers(string):
    parsed_numbers = parse_controll_characters(string)
    
    start = int(parsed_numbers[0])
    end = int(parsed_numbers[1])
    
    return int_range_gen(start=start,end=end)


test_string = "[A-C]"
test_string_number = "[1-3]"

if __name__ == "__main__":
    print(char_range_gen(start="a",end="c"))    
    print(int_range_gen(start=1,end=3))

    print(parse_letters(test_string_number))
    print(parse_numbers(test_string_number))



