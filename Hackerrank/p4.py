# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input("Enter values "))
    arr = map(int, input().split(" "))
    arr = list(arr)
    arr.sort(reverse=True)
    winner = arr[0]
    runner_up = arr[1]
    for i in arr:
        if winner != i:
            print(i)
            break
