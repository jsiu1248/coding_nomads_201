# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

#is there a difference?

string = "codingnomads"

#string_tup=tuple(string)
string_tup=("c","o","d","i")

for i in string:
    print(i)


for i in string_tup:
    print(i)