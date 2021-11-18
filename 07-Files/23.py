import csv

with open("file23.txt", "r") as file:
    row_num=0
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if(row_num>0):
            if(int(row[2])<30):
                print('{:<8} {:<8} {:<10}'.format(row[0], row[1], row[4]))
        row_num+=1