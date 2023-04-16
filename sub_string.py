s = input("Please type in a string: ")
i = 1
cnt = len(s) - 1
for i in range(len(s)):
    j = cnt
    while(j < len(s)):
        print(s[j], end="")
        j += 1
    cnt -= 1
    print("")
