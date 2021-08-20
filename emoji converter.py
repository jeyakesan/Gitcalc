def emojis (message):
    words = message.split (" ")
    emoji = {
        'happy' : ':)',
        'sad' : ':(',
    }
    output = ""
    for word in words:
        output = output + emoji.get(word , word) + ' '
    return output


message = input (">>" )
print(emojis (message))

