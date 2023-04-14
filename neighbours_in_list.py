
import math
def longest_series_of_neighbours(my_list):
    res = -1 
    temp = 0
    for i in range(0, len(my_list)):
        temp = 0
        for j in range(i + 1, len(my_list)):
            if(abs(my_list[j - 1] - my_list[j]) <= 1):
                temp += 1
            else: 
                break
        res = max(res, temp)
    return res + 1  
    
    
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))


