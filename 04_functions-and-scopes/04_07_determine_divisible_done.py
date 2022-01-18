# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages


def divide_4_and_7 (number):
    number = int(input("Enter a number between 1 and a billion"))
    if number%4==0 and number%7==0 and number>0 and number<=1000000000:
        print(f"{number} is divisible by 4 and 7.")
        #return True
    else:
        print(f"{number} isn't divisble by 4 and 7")


def divide_4_or_7(number):
    number = int(input("Enter a number between 1 and a billion"))
    if (number%4==0 or number%7==0) and number>0 and number<=1000000000:
        print(f"{number} is divisible by 4 or 7.")
        #return True
    else:
        print(f"{number} isn't divisble by 4 or 7")




divide_4_or_7(4)
divide_4_and_7(4)