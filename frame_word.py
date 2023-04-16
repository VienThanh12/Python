s = input("Word: ")
i = 1
for i in range(30):
    print("*", end="")
print("")
print("*", end="")
cnt = int((30 - 2 - len(s)) / 2)
i = 1
for i in range(cnt):
    print(" ", end="")
print(s, end="")
for i in range(30 - cnt - 2 - len(s)):
    print(" ", end="")
print("*")

for i in range(30):
    print("*", end="")
