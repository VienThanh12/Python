def length_of_longest(my_list):
    res = -1
    for i in range(0, len(my_list)):
        res = max(res, len(my_list[i]))
    return res
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
