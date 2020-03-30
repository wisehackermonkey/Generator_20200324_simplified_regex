
import random
import string
import sys
import re  # for regex


class generator():
    string = ""
    def __init__(self, string):
        self.string = self.parse_multiple(string)
    def get(self):
        return self.string
    def parse_char_selection(self, string):
        # if "-" in string:
        # if contains repeated chars: -> error
        parsed_selection = self.parse_controll_characters(string) 
        random_selection = random.choice(list(parsed_selection[0])) 
        return random_selection

    def parse_parens_one(self, _string):
        return self.parse_parens(_string)[-1]

    def parse_multiple(self, _string):

        
        if self.check(self.remove_controll_characters(_string)): # is balanced control characters
            result = ""
            # split on [][]
            #          []()[]()
            parsed_brackets = self.parse(_string,r'\[\]')
            
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
                        if parse_dash[0].isnumeric() and parse_dash[1].isnumeric():
                            start = int(parse_dash[0])
                            end = int(parse_dash[1])
                            letter = str(self.int_range_gen(start=start, end=end))
                        elif parse_dash[0].isalpha() and parse_dash[1].isalpha():
                            letter = self.char_range_gen(start=parse_dash[0], end= parse_dash[1])
                        #"[s,s,s]" include , & not include \, & does include multiple ","
                        #"[*1\,3]" include , & includes \,    & does not iclude multiple ","
                    #checks for this pattern "\,abc123" excludes this pattern "[a,b,cd]"
                    elif not self.is_short_hand(command):
                        letter = self.parse_char_selection(command)
                    elif self.is_short_hand(command):
                        print("TODO")

                result += letter
            return result

        return "Unbalanced Brackets!"


    def char_range_gen(self, start="", end=""):
        # if start != "" and end != "":

        start_range = ord(start)
        # the plus +1 makes the range include the end value in the random selection of letters
        stop_range = ord(start) + (ord(end) - ord(start))+1
        return chr(random.randrange(start_range, stop_range))

    def int_range_gen(self, start=0, end=0):
        return random.randrange(start, end + 1)

    def parse(self, _string, _regex):
        regex_expression = fr'[{ _regex }\s]\s*'

        parsed_string = re.split(regex_expression, _string)

        removed_empties = list(filter(None, parsed_string))
        return removed_empties

    def parse_controll_characters(self, _string):
        return self.parse(_string, r"-\[\]")

    def parse_parens(self, _string):
        # if "(" or ")" in string

        return self.parse(_string, r'-\[\]()')

    def parse_brackets(self, _string):
        return self.parse(_string, r'[\[\]')[-1]

    def string_contains_letters(self, _string):
        return bool(re.search('[a-zA-Z]', _string))

    def contains_escaped_controll_chars(self, _string):
        return any(item in _string for item in (r"\(", r"\)", r"\[", r"\]", r"\,", r"\\"))

    def is_short_hand(self, _string):
        for controll_char in (r"\(", r"\)", r"\[", r"\]", r"\,", r"\\"):
            _string = _string.replace(controll_char, "")
        contains_list_short_hand = "," in _string
        return contains_list_short_hand

    def remove_letters(self, _string):
        import string

        if self.string_contains_letters(_string):
            letters = string.ascii_letters + "-,"
            return _string.translate({ord(i): None for i in letters})
        return _string

    def remove_non_controll_characters(self, _string):
        result = ""
        for char in _string:
            if char in r"\(\)\[\]\,\\":
                result += char
        return result

    def remove_controll_characters(self, _string):
        result = ""
        for char in _string:
            if not char in r"\(\)\[\]\,\\":
                result += char
        return result
    # check if there is a balanced controll characters ), ], (, [ in str
    # https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/

    def check(self, my_string):
        import string
        # if empty
        # if only letters
        my_string = self.remove_non_controll_characters(my_string)
        brackets = ['()', '{}', '[]']
        while any(x in my_string for x in brackets):
            for br in brackets:
                my_string = my_string.replace(br, '')
        return not my_string

    def parse_letters(self, string):
        removed_empties = self.parse_controll_characters(string)
        
        start_range = removed_empties[0]
        end_range = removed_empties[1]
        
        return self.char_range_gen(start=start_range,end=end_range)


    def parse_numbers(self, string):
        parsed_numbers = self.parse_controll_characters(string)
        
        start = int(parsed_numbers[0])
        end = int(parsed_numbers[1])
        
        return self.int_range_gen(start=start,end=end)
