# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(inp):
    result = ""
    for c in inp:
        if c.islower():
            c = c.upper()
            result = result + c
        else:
            c = c.lower()
            result = result + c
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

