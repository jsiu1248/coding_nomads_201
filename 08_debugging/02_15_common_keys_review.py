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


#dict_3 = dict_1.copy()
"""
for key,value in dict_2.items():
    if key in dict_3:
        dict_3[key]=dict_3[key]+dict_2[key]
    else:
        dict_3[key]=value
print(dict_3)
"""
dict_4={}

dict_merge=[dict_1,dict_2]
print(dict_merge)

for i in dict_merge:
    for key, value in i.items():
        if key in dict_4:
            dict_4[key]=dict_4[key]+i[key]
        else:
            dict_4[key]=value
print(dict_4)
# I did this better because I started with a blank slate and converted into a list that has both dictionaries and then looped them both