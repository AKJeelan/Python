# Write a program to remove duplicates in the list


list = [1,2,3,3,4,5,5,5,6,7,8,9,9,10]

# for numbers in list:
#     count = 0
#     for item in list:
#         if(numbers == item):
#             count += 1
#         if(count > 1):
#             list.remove(item)
#             count -= 1
# print(list)

list.sort();

for index in range(1,len(list)):
    if(list(index) == list(index - 1)):
        list.pop(index)
        
        

