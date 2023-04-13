# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(text):
    n = len(text)
    for i in range(0, n):
        n -= 1
        if(text[i] != text[n]):
            return False
    return True




while(True):
    word = input("Please type in a palindrome: ")
    if(palindromes(word) == False):
        print("that wasn't a palindrome")
    else:
        print(f"{word} is a palindrome!")
        break
