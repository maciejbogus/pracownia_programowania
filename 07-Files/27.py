import re
with open("file27.txt", "r") as file:
    text = file.read()
    words = re.findall("[a-zA-z]{6,}",text)
    
for word in words:
    print(word)