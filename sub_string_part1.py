s = input("Please type in a string: ")
i = 1
cnt = 1
for i in range(len(s)):
    j = 0
    for j in range(cnt):
        print(s[j], end="")
    cnt += 1
    print("")
