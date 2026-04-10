# def square(number):
#     return number * number;

# number = 10;
# result = square(10);

# print(result)

# Postional & Keyword argument

def greeting(first_name,last_name):
    print(f"Good Morning {first_name} {last_name}, How are you ?")

first_name = "Abdul"
last_name = "Jeelan"

greeting(first_name="Jeelan",last_name="Abdul")
# greeting(first_name="Abdul",last_name) # Error first paramter type can't be keyword arguement


# Rewriting emojis_converter using functions.

def emojis_converter(message):
    emojis = {
        ":)" : "😃",
        ":(" : "😞"
    }
    message = message.split(' ')
    output = ""
    for word in message:
        output += emojis.get(word, word) + ' '
    return output

message = input(">")
result = emojis_converter(message)
message = input(">")
result = emojis_converter(message)


print(result)