# Using the given variables `base` and `digits`, write a dictionary comprehension
# that maps each integer between `0` and `999` to the list of three digits 
# that represents that integer in base 10. That is, the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 0, 2], 3: [0, 0, 3], ...,
# 10: [0, 1, 0], 11: [0, 1, 1], 12: [0, 1, 2], ...,
# 999: [9, 9, 9]}
#
# Your expression should work for any base. For example, 
# if you instead assign 2 to base and assign {0,1} to digits, 
# the value should be:
#
# {0: [0, 0, 0], 1: [0, 0, 1], 2: [0, 1, 0], 3: [0, 1, 1],
# ..., 7: [1, 1, 1]}

base = 3
digits = set(range(base))
print(digits)


#dictionary comprehension
#maps each integer 0 and 999

dictcomp= {k:[k//base//base%base, k//base%base,k%base] for k in range(101) if k<=base**3-1}
print(dictcomp)

#dictcomp={k:k for k in list(range(101)) for k in str(k)}
#dictcomp={k:str(k) for k in range(101)}

#print(dictcomp)
#string representation of digits
# if the first and second number is less than 10
#i can iterate through a string/value or variable
#['1','2'.'3']
#dict={}
#for i in range(101):
#    dict[i]=str(i)

#print(dict)

#a = 001
#b = '001'
#print(b)
#print(a)
