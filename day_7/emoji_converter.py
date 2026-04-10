# Press ctrl + i to bring emoji popup


message = input(">")

emojis = {
    ":)" : "😃",
    ":(" : "😞"
}

message = message.split(' ')

output = ""
for word in message:
    output += emojis.get(word, word) + ' '
print(output)