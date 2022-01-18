# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

file_in = open("words.txt", "r")

contents = file_in.read()
contents=contents.splitlines()
#print(type(contents))
#print(contents)
for i in contents:
    if len(i)>20:
        print(i)