from ast import While
from ctypes.wintypes import tagRECT
from xml.dom.minidom import Element


def binary_search(list, target):
    sorted_list = list.sort()
    start = 0
    middle = 0
    end = len(list)
    steps = 1

    while (start <= end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps += 1
        middle = (start + end) // 2

        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = [65, 61, 96, 3, 13, 95, 99, 41, 59, 85, 39, 88, 1, 48, 60, 66, 31, 27, 12, 36, 71, 33, 87, 35, 56, 86, 55, 68, 5, 43, 98, 46, 69, 17, 15, 58, 73, 19, 90, 50, 9, 8, 74, 62, 42, 80, 78, 38, 20,
           67, 53, 91, 10, 83, 89, 92, 75, 81, 4, 72, 97, 14, 25, 54, 40, 79, 24, 29, 34, 51, 49, 44, 6, 77, 22, 2, 37, 23, 100, 70, 30, 47, 28, 84, 11, 82, 57, 63, 52, 32, 93, 45, 94, 76, 18, 26, 7, 21, 16, 64]
target = 50

binary_search(my_list, target)
