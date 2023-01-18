def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    else:
        return -1


def binary_search(list, target):
    high = len(list) - 1
    low = 0
    mid = 0
    while high >= low:
        mid = (high + low) // 2

        if list[mid] == target:
            return mid
        elif list[mid] > target:
            high = mid - 1
        elif list[mid] < target:
            low = mid + 1
    else:
        return -1
