# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.
def real_estate (*args):
    for i in args:
        print(f"{i}")
print("Welcome to this house that is going to be the best choice for you.")


real_estate("Price: 2000000","Bath: 4", "Bed: 4", "Backyard: Yes", "Garage: 2")

