PIN = "0805"
for i in range(0, 3):
    enteredPIN = input("Enter the PIN code: ")
    if(enteredPIN != PIN):
        print("Incorrect...")
        if(i==2): print("Sorry, your card has been blocked...")
    else: 
        print("Correct")
        break