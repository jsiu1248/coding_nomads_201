# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

file_in = open("words.txt", "r")

contents = file_in.read()
contents=contents.splitlines()
print(contents)

minimum = list()
maximum = list()
for i in contents:
    length = len(i)
    minimum.append(length)
    maximum.append(length)
minimum = (min(minimum))
maximum = (max(maximum))

for i in contents:
    if len(i)==minimum:
        print(i)
    elif len(i)==maximum:
        print(i)
print(len(contents))



# is there a quicker way to do this?

