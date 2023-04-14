
num = int(input("How many items: "))
myList = []
for i in range(0, num):
    x = int(input(f"Item {i + 1}: "))
    myList.append(x)
print(myList)
