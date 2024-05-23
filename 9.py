# Question 5:
# Recommended time: 8 min
# Print the sum of the current number and the previous
# number
# Write a program to iterate the first 10 numbers and in each iteration, print the
# sum of the current and previous number.
for i in range(0,10):
    if i == 0:
     print("current number : ", i, "previous number :", i, "sum :",i)
    elif i != 0:
        print("current number : ", i, "previous number :", i-1, "sum :",i+i-1)