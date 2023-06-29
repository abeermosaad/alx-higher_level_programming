#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for ele in my_list:
            if (cnt >= x):
                break
            print("{}".format(ele), end="")
            cnt += 1
        print("".format())
        return cnt
    except ValueError:
        print("ValueError error")
