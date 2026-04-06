
# Math Functions
# Ask the user for two numbers. Print the floor, ceiling, absolute value, and which number is larger (use max/min).

import math;

num1 = input('Enter number 1 : ')
num2 = input('Enter number 2 : ')

num1 = float(num1);
num2 = float(num2);

print(math.floor(num1)) # return largest integer <= of number
print(math.ceil(num2)) # return smalles integer >= of number

abs(num2) # retruns the distance from zero
min(num1,num2) # works with strings, number
max(num1,num2) # works with strings, number

# inputs
# try with both positive and negative number