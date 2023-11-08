#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    wei = 0
    ave = 0

    for tup in my_list:
        wei += tup[0] * tup[1]
        ave += tup[1]

    return (wei / ave)

