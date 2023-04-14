def all_the_longest(my_list):
    res = -1
    new_list = []
    for i in range(0, len(my_list)):
        res = max(res, len(my_list[i]))
    for i in range(0, len(my_list)):
        if(len(my_list[i]) == res):
            new_list.append(my_list[i])
    return new_list
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)
