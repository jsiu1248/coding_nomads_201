# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1


ten_list=[]
for i in range(11):
    ten_list.append(int(input("Enter a number: ")))
    #number= int(input("Enter a number: "))
    #ten_list.append(number)
    #why doesn't this work?
print(f"{ten_list[1]},{ten_list[3]},{ten_list[5]}, {ten_list[7]}, {ten_list[9]}, {ten_list[6]}, {ten_list[4]}, {ten_list[2]}, {ten_list[0]}         ")