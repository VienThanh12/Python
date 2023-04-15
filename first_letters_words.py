sen = input("Please type in a sentence: ")
print(sen[0])
for i in range(len(sen)):
	if(sen[i - 1] == ' '):
		print(sen[i])
