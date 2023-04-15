num = int(input("Please type in a number: "))

end = num
for i in range(1, int(num / 2) + 1):
	print(i)
	print(end)
	end = end - 1
if(num % 2 == 1):
	print(int((num + 1) / 2))
