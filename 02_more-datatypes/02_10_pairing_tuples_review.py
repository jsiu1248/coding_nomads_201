# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources_done import randlist

print(randlist)

# Write your code below here
randlist.sort()
print(randlist)
two_tuples=[]
print(len(randlist))
#for i in randlist:
# #for i in range(0, len(randlist), 2):
for i in range(0, len(randlist), 2):
    if len(randlist)%2==1 and i==(len(randlist)-1):
        two_tuples.append((randlist[i],0))
    else:
        two_tuples.append((randlist[i],randlist[i+1]))

print(two_tuples)


#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.

