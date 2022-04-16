if __name__ == '__main__':
    lst = [9, 5, 8, 3, 6, 7, 1, 5, 4]
    lowest = lst[0]
    for i in lst:
        if lowest < i:
            lowest = i
        else:
            lowest = lowest