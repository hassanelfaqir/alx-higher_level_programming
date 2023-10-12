#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    list_a = list(new_d.keys())

    for i in list_a:
        new_d[i] *= 2

    return (new_d)
