# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}
dict_key=list(range(1,11))
dict_values=[i**2 for i in dict_key]
#I wonder why it isn't easier to **2 a list.
print(dict_key)
print(dict_values)


dictionary={dict_key[i]:dict_values[i] for i in range(len(dict_key))}

print(dictionary)

