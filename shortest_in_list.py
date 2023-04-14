def shortest(my_list):
    res = 999999
    for i in range(0, len(my_list)):
        res = min(res, len(my_list[i]))
    for i in range(0, len(my_list)):
        if(len(my_list[i]) == res):
            return my_list[i]
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
