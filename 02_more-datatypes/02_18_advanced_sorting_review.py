# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

#turn dictionary into tuple

sorted_keys=sorted(input_dict, key=input_dict.get) #return a list of keys whose values are sorted in order

sorted_dict={}
sorted_list=[]
for i in sorted_keys: # for each sort number
    sorted_dict[i]=input_dict[i] # make empty dict find the value input_dict


for j in sorted_dict.items():
    sorted_list.append(j,)
print(sorted_list)
