#!/usr/bin/python3
def to_subtract(list_num):
    to_s = 0
    max_l = max(list_num)

    for n in list_num:
        if max_l > n:
            to_s += n

    return (max_l - to_s)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_nm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_k = list(rom_nm.keys())

    number = 0
    last_r = 0
    list_n = [0]

    for cha in roman_string:
        for r_number in list_k:
            if r_number == cha:
                if rom_nm.get(ch) <= last_r:
                    number += to_subtract(list_n)
                    list_n = [rom_nm.get(cha)]
                else:
                    list_n.append(rom_nm.get(cha))

                last_r = rom_nm.get(cha)

    number += to_subtract(list_n)

    return (number)
