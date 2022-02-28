def average(array):
    unique_arr = set()
    average_result = 0
    for i in array:
        unique_arr.add(i)
    for i in unique_arr:
        average_result = (i / len(unique_arr)) + average_result
    return average_result




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)