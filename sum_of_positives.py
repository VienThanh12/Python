# Write your solution here

def sum_of_positives(my_list):
    cnt = 0
    for i in range(0, len(my_list)):
        if(my_list[i] > 0):
            cnt += my_list[i]
    return cnt

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
