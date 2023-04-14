import math
def formatted(my_list):
    new = []
    for i in range(0, len(my_list)):
        number = my_list[i]
        #print(f"{number:.2f}")
        #print(number)
        new.append(f"{number:.2f}")
    return new
if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
