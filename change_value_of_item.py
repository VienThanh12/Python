
index = 0
myList = [1, 2, 3, 4, 5]
while(index != -1):
    index = int(input("Index: "))
    if(index == -1):
        break
    new_val = int(input("New value: "))
    myList[index] = new_val
    print(myList)
