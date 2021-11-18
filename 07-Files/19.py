shopping_file = open('shoppinglist.txt','a')
file1 = open('GrainsAndBread.txt','r')
file2 = open('MeatAndFish.txt','r')

shopping_file.write(file1.read())
shopping_file.write(file2.read())

shopping_file.close()
file1.close()
file2.close()