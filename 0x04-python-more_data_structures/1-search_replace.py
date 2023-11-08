#!/usr/bin/python3
def search_replace(my_list, search, replace):
    y_list = list(my_list)
    for i in range(len(y_list)):
        if y_list[i] == search:
            y_list[i] = replace
    return y_list
