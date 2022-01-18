# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

generator = (x*5 for x in range(10))
print(generator)


for i in generator:
    print(i)

