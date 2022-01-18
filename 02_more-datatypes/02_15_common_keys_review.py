# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

dict_3=dict_1.copy()
print(dict_3)
for key, value in dict_2.items():
    #copy of dict1 and then looping through dict2. So, if it is in dict3 then sum. If it isn't in dict3 then add the dict2 key, value
    if key in dict_3:
        dict_3[key]=dict_3[key]+dict_2[key]
    else:
        dict_3[key]=value
print(dict_3)