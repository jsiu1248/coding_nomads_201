# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(*args):  # add your arguments
      index=0
      for value in args:

            print(index,value)
            index = index + 1 # if I put this before the print then it would return 1 for the first item which is too quick


my_enumerate("text","hi","word","what","up")

#iterable as an input
#gives back both the element as well as the index position