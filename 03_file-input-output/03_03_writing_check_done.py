# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.
file_in = open("words.txt", "r")

contents = file_in.read()
contents=contents.splitlines()

# do I reserved the words or just the list?
backward = open("contents_backwards.txt", "w")
#.reverse changes it into Nonetype
contents_backward=contents[::-1]
print(type(contents_backward))
backward.writelines(str(contents_backward))
backward.close()
#print(contents)
