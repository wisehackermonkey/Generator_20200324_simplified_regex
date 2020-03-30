#Simplified regex text generator 
#20200324
#by oran collins

import random
import string
import sys

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

def parse(_string, _regex):
    regex_expression = fr'[{ _regex }\s]\s*'
    
    parsed_string = re.split(regex_expression, _string)

    removed_empties = list(filter(None, parsed_string))
    return removed_empties


def parse_controll_characters(_string):
    return parse(_string,r"-\[\]")
    
    
def parse_parens(_string):
    # if "(" or ")" in string
    
    return parse(_string,r'-\[\]()')

def parse_brackets(_string):
    return parse(_string,r'[\[\]')[-1]


def string_contains_letters(_string):
    return bool(re.search('[a-zA-Z]', _string))

#"\( \) \[ \] \, \\ \\\ " ( includes "\(" or includes "\]" or... ) or True &  does not include \\\\\ x5

# [\(  \) \[ \]  \,] not include unescaped controll characters (){},\

# examples
# [abbc\[cc]  true
# [\(\)\[\]\,]  true

# [abb,ccc]  false
# [abbccc]  false

# [abb,cc\(c] true

def contains_escaped_controll_chars(_string):
    return any(item in _string for item in (r"\(", r"\)", r"\[", r"\]", r"\,", r"\\"))


def is_short_hand(_string):
    for controll_char in (r"\(", r"\)", r"\[", r"\]", r"\,", r"\\"):
        _string = _string.replace(controll_char,"")
    contains_list_short_hand = "," in _string
    return contains_list_short_hand
# [abb,cc\(c] contains escaped controll chars == true, and contains 1 []()\ and contains 0 or more 

# [abb,cc\(c] remove controll characters, contains 1 or more "," characters , contains 1 of contains 1 []()\
# [abb,ccc]  


def remove_letters(_string):
    import string

    if string_contains_letters(_string):
        letters = string.ascii_letters + "-,"
        return _string.translate({ord(i): None for i in letters})
    return  _string

def remove_non_controll_characters(_string):
    result = ""
    for char in _string:
        if char in r"\(\)\[\]\,\\":
            result += char
    return result
def remove_controll_characters(_string):
    result = ""
    for char in _string:
        if not char in r"\(\)\[\]\,\\":
            result += char
    return result
# check if there is a balanced controll characters ), ], (, [ in str 
#https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
def check(my_string): 
    import string
    # if empty
    #if only letters
    my_string = remove_non_controll_characters(my_string)
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   

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

def parse_char_selection(string):
    # if "-" in string:
    # if contains repeated chars: -> error
    parsed_selection = parse_controll_characters(string) 
    random_selection = random.choice(list(parsed_selection[0])) 
    return random_selection

def parse_parens_one(_string):
    return parse_parens(_string)[-1]

def parse_multiple(_string):

    
    if check(remove_controll_characters(_string)): # is balanced control characters
        result = ""
        # split on [][]
        #          []()[]()
        parsed_brackets = parse(_string,r'\[\]')
        
        for command in parsed_brackets:
            letter = ""
            # TODO add more strict criteria ei command[-1] and [0]
            is_command  = bool(command[0] == "(" and command[-1] ==  ")")

            if is_command: # its a controll command ex: (TAB) 
                return "works: TODO command parse"
            else: # if its [A-Z] or [1-9]

                # if command includes non escaped "\" character
                if "-" in command:
                    # account for including "-" 
                    parse_dash = command.split("-")
                    letter = char_range_gen(start=parse_dash[0], end= parse_dash[1])
                    #"[s,s,s]" include , & not include \, & does include multiple ","
                    #"[*1\,3]" include , & includes \,    & does not iclude multiple ","
                #checks for this pattern "\,abc123" excludes this pattern "[a,b,cd]"
                elif not is_short_hand(command):
                    letter = parse_char_selection(command)
                elif is_short_hand(command):
                    print("TODO")

            result += letter
        return result

    return "Unbalanced Brackets!"


test_string = "[A-C]"
test_string_number = "[1-3]"
test_string_char_selection = "[Ac4]"
test_string_controll_parens = "[1-3](command)"
test_string_controll_parens_v2 = "(command2)"
test_string_breakets = "[asdfads]"

test_string_multiple= "[A-C](command)[A-C]"
test_string_multiple2= "[[]()[]]"
test_string_multiple_only_brackets= "[A-C][A-C]"
test_string_multiple_only_brackets2= "[A-C][sts][A-C]"
test_string_multiple_only_brackets_unbalanced= "[A-C][A-C]]"
test_string_multiple_with_parens = "[A-C]()[A-C]()"
test_string_list_shorthand = "[AA,AA]"
test_string_list_shorthand_true_v1 = r"[AA,A\,A]"
test_string_list_shorthand_false = "[AAAA]"
test_string_list_shorthand_false2 = r"[AAA\(A]"
test_string_multiple_list_shorthand_true_v1 = r"[acb][123][X-Z]"
test_string_multiple_list_shorthand_true_v2 = r"[\,\(\[][123][X-Z]"

def formater(func,_string):
    print(f"{func.__name__:<30}: {_string:<30} => {func(_string)}")


if __name__ == "__main__":
    # print(char_range_gen(start="a",end="c"))    
    # print(int_range_gen(start=1,end=3))

    # formater(parse_letters, test_string_number)
    # formater(parse_numbers, test_string_number)
    # formater(parse_char_selection, test_string_char_selection)
    # formater(parse_parens_one, test_string_controll_parens)
    # formater(parse_parens_one, test_string_controll_parens_v2)
    # formater(parse_controll_characters, test_string_multiple)
    # formater(parse_controll_characters, test_string_multiple2)
    # formater(parse_brackets, test_string_breakets)

    # # Driver code 
    # # string = "{[]{()}}"
    # string = test_string_multiple
    # print(string, "-", "Balanced" if check(string) else "Unbalanced") 
    # formater(remove_letters,  test_string_multiple)
    # formater(remove_letters,  test_string_multiple2)
    # formater(parse_multiple,  test_string_multiple_only_brackets)
    # formater(parse_multiple,  test_string_multiple_only_brackets2)
    # formater(parse_multiple,  test_string_multiple_only_brackets_unbalanced)
    # formater(parse_multiple,  test_string_multiple_with_parens)
    # formater(is_short_hand,  test_string_list_shorthand)
    # formater(is_short_hand,  test_string_list_shorthand_false)
    # formater(is_short_hand,  test_string_list_shorthand_false2)
    # formater(is_short_hand,  test_string_list_shorthand_true_v1)
    # formater(parse_multiple,  test_string_multiple_list_shorthand_true_v1)
    # formater(remove_non_controll_characters, "[A-C](command)[A-C]")
    # formater(parse_multiple, test_string_multiple_list_shorthand_true_v2)
    
    if len(sys.argv) >=2:
        command  = sys.argv[1]


        # TODO fix phone number & imbeding
        # command = "([1-9][A-Z][1-9])-([1-9][A-Z][1-9])"
        result = parse_multiple(command)
        print(sys.argv[-1])
        print(f"Result: {command} => {result}")
    else:
        print("no Args")
        print('please run something like > python Generator.py "\([1-9][A-Z][1-9]\)" ')
    
    


