# simple test function code, NOTE:does not do validation
# by oran collins
# 20200329
from generator import generator


gen = generator("[1-255].[1-255].[1-255].[1-255]")

print(gen.get())

def formater(func,_string):
    if len(_string) <= 0:
        print(f"{func.__name__:<30}: {_string:<30} => {func()}")
    else:
        print(f"{func.__name__:<30}: {_string:<30} => {func(_string)}")




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


# print(gen.char_range_gen(start="a",end="c"))    
# print(gen.int_range_gen(start=1,end=3))
# # Driver code 
# # string = "{[]{()}}"
string = test_string_multiple
print(string, "-", "Balanced" if gen.check(string) else "Unbalanced")
print("-----------------")

formater(gen.parse_letters, test_string_number)
formater(gen.parse_numbers, test_string_number)
formater(gen.parse_char_selection, test_string_char_selection)
formater(gen.parse_parens_one, test_string_controll_parens)
formater(gen.parse_parens_one, test_string_controll_parens_v2)
formater(gen.parse_controll_characters, test_string_multiple)
formater(gen.parse_controll_characters, test_string_multiple2)
formater(gen.parse_brackets, test_string_breakets)

 
formater(gen.remove_letters,  test_string_multiple)
formater(gen.remove_letters,  test_string_multiple2)
formater(gen.parse_multiple,  test_string_multiple_only_brackets)
formater(gen.parse_multiple,  test_string_multiple_only_brackets2)
formater(gen.parse_multiple,  test_string_multiple_only_brackets_unbalanced)
formater(gen.parse_multiple,  test_string_multiple_with_parens)
formater(gen.is_short_hand,  test_string_list_shorthand)
formater(gen.is_short_hand,  test_string_list_shorthand_false)
formater(gen.is_short_hand,  test_string_list_shorthand_false2)
formater(gen.is_short_hand,  test_string_list_shorthand_true_v1)
formater(gen.parse_multiple,  test_string_multiple_list_shorthand_true_v1)
formater(gen.remove_non_controll_characters, "[A-C](command)[A-C]")
formater(gen.parse_multiple, test_string_multiple_list_shorthand_true_v2)

formater(gen.get, "")
