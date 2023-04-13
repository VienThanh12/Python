def distinct_numbers(my_list):
    cnt = []
    new_list = []
    for i in range(0, 10000):
        cnt.append(0)

    for i in range(0, len(my_list)):
        #print(my_list[i])
        if(cnt[my_list[i]] == 0):
            new_list.append(my_list[i])
            cnt[my_list[i]] += 1
    #print(new_list)
    new_list.sort()
    return new_list
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
