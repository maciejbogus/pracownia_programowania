def how_many_letters(text, letter):
    count=0
    for i in range(0, len(text)):
        if text[i]==letter: 
            count+=1
    if(count!=0):
        return count
    else:
        return "Not found"

x = input("Enter finding letter: ")

text = "You never get a second chance to make a first impression"

print(how_many_letters(text, x))