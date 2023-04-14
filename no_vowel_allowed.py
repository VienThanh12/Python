

def no_vowels(my_string):
    new_string = ""
    for i in range(0, len(my_string)):
        if(my_string[i] == 'u' or my_string[i] == 'e' or my_string[i] == 'o' or my_string[i] == 'a' or my_string[i] == 'i'):
            continue
        new_string = new_string + my_string[i]
    return new_string
    
if __name__ == "__main__":
    fmy_string = "this is an example"
    print(no_vowels(fmy_string))

