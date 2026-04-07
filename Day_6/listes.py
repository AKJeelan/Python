# write a program to find largest number in the list

numbers = [1,2,10,0,2,8,1,19]
largest_number = 0;

for num in numbers:
    if(num > largest_number):
        largest_number = num
print(largest_number)