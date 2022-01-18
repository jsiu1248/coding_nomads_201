# Adapt your Generator expression from the previous exercise:
# Don't print anything, and run a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)

generator = (i for i in nums if i//1111==0)

for j in generator:
    print(j)
