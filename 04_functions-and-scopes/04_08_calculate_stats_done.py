# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

#min(example) vs example.min()

def stats():
    minimum=min(example_list)
    maximum=max(example_list)
    average=sum(example_list)/len(example_list)
    summation=sum(example_list)
    print(minimum)
    print(maximum)
    print(average)
    print(summation)
# call the function below here



stats()