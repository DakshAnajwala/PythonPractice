def average(array):
    unique_arr = set()
    average_result = 0
    sum = 0
    for i in array:
        unique_arr.add(i)
    for i in unique_arr:
        sum = i + sum
    average_result = sum / len(unique_arr)
    return average_result




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)