def numbers():
    for i in range(1, 10, 3):
        for j in range(0, 3):
            print(i+j, end=" ")
        print()

numbers()