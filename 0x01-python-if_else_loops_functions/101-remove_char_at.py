#!/usr/bin/python3
def remove_char_at(str, n):
    str_new = ''
    i = 0
    for char in str:
        if i != n:
            str_new = str_new + str[i]
        i = i + 1
    return (str_new)
