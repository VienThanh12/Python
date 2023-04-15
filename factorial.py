#num = int(input("Please type in a number: "))
num = 1
while(num > 0):
	num = int(input("Please type in a number: "))
	if(num <= 0):
		break
	res = 1
	for i in range(num):
		res = res * (i + 1)
	print(f"The factorial of the number {num} is {res}")
print("Thanks and bye!")
