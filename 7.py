# Question 3:
# Recommended time: 7 min
# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String: 'abc', 'xyz'
# Expected Result: 'xyc abz'
# x=input("")
# y=input("")
# a,b=x[0],y[0]
# #print(b+y[:-1]+" "+a+x[:-1])
# #print(a+y+" "+b+x)
# print(y[:-1])
# a=input("")
# b=input("")
# #print(a[:-1]+b[2], " ", b[:-1]+a[2])
# print(b[0]+a[1:2], " ", a[0]+b[1:2])
#


a=input("")
b=input("")
print(b[:-1]+a[2], " ", a[:-1]+b[2])