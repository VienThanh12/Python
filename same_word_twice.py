myList = []
res = 0
while True:
    word = str(input("Word: "))
    if word in myList:
        print(f"You typed in {res} different words")
        break
    myList.append(word)
    res += 1    
    #print(myList)
    #break
