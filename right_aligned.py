s = input("Please type in a string: ")
cnt = 20 - len(s)

for i in range(cnt):
    print("*", end="")
print(s)
