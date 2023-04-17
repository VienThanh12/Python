import math
def first_word(text):
    res = ""
    for i in range(0, len(text)):
        if(text[i] == ' '):
            return str(res)
            break
        else:
            res += text[i] 
def second_word(text):
    cnt = 0
    res = ""
    for i in range(0, len(text)):
        if(text[i] == ' ' and cnt == 0):
            cnt += 1
            res = ""
        elif (cnt == 1 and text[i] == ' '):
            return str(res)
        else:
            res += text[i] 
    return str(res)
def string_to_int(text):
    #print(text[1])
    num_1 = 0
    num_2 = 0
    if(text == '100'):
        return 100
    text = text + '00000'
    if(text[0] == '1'):
        num_1 = 1
    if(text[0] == '2'):
        num_1 = 2
    if(text[0] == '3'):
        num_1 = 3
    if(text[0] == '4'):
        num_1 = 4
    if(text[0] == '5'):
        num_1 = 5
    if(text[0] == '6'):
        num_1 = 6
    if(text[0] == '7'):
        num_1 = 7
    if(text[0] == '8'):
        num_1 = 8
    if(text[0] == '9'):
        num_1 = 9
    if(len(text) > 6):
        if(text[1] == '0'):
            num_2 = 0
        if(text[1] == '1'):
            num_2 = 1
        if(text[1] == '2'):
            num_2 = 2
        if(text[1] == '3'):
            num_2 = 3
        if(text[1] == '4'):
            num_2 = 4
        if(text[1] == '5'):
            num_2 = 5
        if(text[1] == '6'):
            num_2 = 6
        if(text[1] == '7'):
            num_2 = 7
        if(text[1] == '8'):
            num_2 = 8
        if(text[1] == '9'):
            num_2 = 9
    if(len(text) > 6):
        return num_1 * 10 + num_2
    else:
        return num_1

point_ave = 0
cnt = 0
grade_5 = 0
grade_4 = 0
grade_3 = 0
grade_2 = 0
grade_1 = 0
fail = 0
fail_student = 0
pass_ = 0
def print_char(num):
    for i in range(0, num):
        print("*", end ="")
while(True):
    input_ = str(input("Exam points and exercises completed: "))
    fir_num = str(first_word(input_))
    se_num = str(second_word(input_))
    num_fi = 0
    num_se = 0
    num_fi = string_to_int(fir_num)
    num_se = string_to_int(se_num)
    if(input_ == ""):
        print("Statistics:")
        point_ave = point_ave / cnt
        print("Points average:",point_ave)
        #print(fail_student)
        #print(fail)
        pass_ = cnt 
        pass_ = pass_ - fail
        pass_ = pass_ / cnt * 100
        print("Pass percentage:", f"{pass_:.1f}")
        print("Grade distribution:")
        print("  5: ", end = "")
        print_char(grade_5)
        print("")
        print("  4: ", end = "")
        print_char(grade_4)
        print("")
        print("  3: ", end = "")
        print_char(grade_3)
        print("")
        print("  2: ", end = "")
        print_char(grade_2)
        print("")
        print("  1: ", end = "")
        print_char(grade_1)
        print("")
        print("  0: ", end = "")
        print_char(fail)
        print("")
        break
    cnt += 1
    point_ave = point_ave + num_fi + math.floor(num_se / 10)
    point_ = num_fi + math.floor(num_se / 10)

    if(point_ <= 30 and point_ >= 28 and num_fi >= 10):
        grade_5 += 1
    if(point_ <= 27 and point_ >= 24 and num_fi >= 10):
        grade_4 += 1
    if(point_ <= 23 and point_ >= 21 and num_fi >= 10):
        grade_3 += 1
    if(point_ <= 20 and point_ >= 18 and num_fi >= 10):
        grade_2 += 1
    if(point_ <= 17 and point_ >= 15 and num_fi >= 10):
        grade_1 += 1
    if(point_ <= 14 and point_ >= 0 or num_fi < 10):
        fail += 1
    #print(num_fi)
    #print(num_se)
