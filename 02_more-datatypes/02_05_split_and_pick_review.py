# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.
sentence = input("Write a sentence with multiple repeating words: ")

sentence_list=sentence.split(" ")
print(sentence_list)
dictionary={}


for i in sentence_list:
    if i in dictionary:
        dictionary[i]=dictionary[i]+1
    else:
        dictionary[i]=1

max_key=max(dictionary, key=dictionary.get) # get key with max value

print(max_key)