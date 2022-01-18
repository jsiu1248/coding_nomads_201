# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input=input("Enter text: ")
dictionary={}




for i in user_input:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
        dictionary[i]=1


print(user_input)
print(dictionary)

