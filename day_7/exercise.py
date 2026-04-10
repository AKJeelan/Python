phone_number = input("Phone: ")

# for char in phone_number:
#     if(char == "0"):
#         print("Zero ",end="")
#     if(char == "1"):
#         print("One ", end="")
#     if(char == "2"):
#         print("Two ",end="")
#     if(char == "3"):
#         print("Three ",end="")
#     if(char == "4"):
#         print("Four ",end="")
#     if(char == "5"):
#         print("Five ",end="")
#     if(char == "6"):
#         print("Six ",end="")
#     if(char == "7"):
#         print("Seven ",end="")
#     if(char == "8"):
#         print("Eight ",end="")
#     if(char == "9"):
#         print("Nine ",end="")

# Using dictionary

digit_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three"
}

output = ""
for char in phone_number:
    output += digit_mapping.get(char, "!") + " "
print(output)

