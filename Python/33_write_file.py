text = "\nAppend this text"


with open("text.txt", 'a') as file:
    file.write(text)