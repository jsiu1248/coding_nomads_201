# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
def first(x,y):
    multiple = x*y
    return multiple

def second(x,y):
    add=x+y
    return add

def third(x,y):
    subtract=x-y
    return subtract

def fourth(x,y):
    exp=x**y
    return exp

print(fourth(third(second(first(10,20), 20),10),20))

