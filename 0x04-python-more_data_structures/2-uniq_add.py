#!/usr/bin/python3
def uniq_add(my_list=[]):
    numb = 0
    uniq_List = set(my_list)

    for i in uniq_List:
        numb = numb + i
    return (numb)
