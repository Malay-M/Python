# index operator [] = gives access to a sequence's element (str, list, tuples)

string = "python String"

if string[0].islower():
    string = string.capitalize()


sub_str = string[0:6].upper()

sub_str2 = string[6:].lower()

last_char = string[-1]

print(string)

print(sub_str)

print(sub_str2)

print(last_char)