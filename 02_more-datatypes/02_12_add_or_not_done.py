# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quite the program.
# They wil if they manage to create a set that has more than 10 items.

i=1
set_numbers=set()
count=0
while i==1:
    string=int(input("Keep giving me a number you haven't entered before: "))
    if string in set_numbers:
        print("Sorry. This is an old number and you lose a point.")
        count=count+1
        print(count)
        if count==5:
            print("Sorry you lose. You lost  points.")
            quit()
    elif string not in set_numbers:
        set_numbers.add(string)
