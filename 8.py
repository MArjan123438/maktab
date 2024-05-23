# Question 4:
# Recommended time: 5 min
# Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or
# lower than 1000, else return their sum.
a=int(input())
b=int(input())
c=a*b
if c>1000:
    print(c)
elif c<=1000:
    print(a+b)


