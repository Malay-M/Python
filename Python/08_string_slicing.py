# slicing = create a sub-string by extracting elements from  another string 
#           indexing[] or slice()
#           [start, stop, step]

string = "Hello World"

first_part = string[:5]
last_part = string[6:]

str1 = string[::3]

reversed_str = string[::-1]

print(first_part)
print(last_part)
print(str1)
print(reversed_str)



website1 = "https://google.com/"
website2 = "https://facebook.com/"
slice = slice(8,-5)

print(website1[slice])
print(website2[slice])