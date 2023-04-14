

def most_common_character(my_list):
    num = []
    res = -1
    for i in range(0, len(my_list)):
        res = max(res, my_list.count(my_list[i]))
    for i in range(0, len(my_list)):
        if(res == my_list.count(my_list[i])):
            return my_list[i]
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

