# Take in 10 numbers from the user. Place the numbers in a list.
# You can also use the provided random `randlist` list
# to simulate user input.
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

#from resources import randlist


import random
import math
list_length = 10
randlist = list()
for i in range(list_length):
    number=int(input("Give me a number: "))
    randlist.append(number)
randlist.sort()
sort_list=randlist
largest=sort_list[-1]
product=math.prod(sort_list)


print(sort_list)
print(largest)
print(product)


