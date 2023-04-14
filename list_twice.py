myList = []
sortList = []
while True:
    new_item = int(input("New item: "))
    if(new_item == 0):
        print("Bye!")
        break
    myList.append(new_item)
    sortList.append(new_item)
    print("The list now:", myList)
    sortList.sort()
    print("The list in order:", sortList)
