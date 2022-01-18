# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

string=input("Enter a sentence: ")
string_list=string.split(" ")
string_final=[]
for i in string_list:
    string_final.append(tuple(i))

print(string_final)
