

def no_shouting(my_list):
    new_list = []
    for i in range(0, len(my_list)):
        if(my_list[i].isupper() == False):
            new_list.append(my_list[i])
    
    return new_list
    
    
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)


