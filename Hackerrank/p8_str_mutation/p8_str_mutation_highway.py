# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    mutated_str = ''
    for index in range(len(string)):
        if index == position:
            mutated_str = mutated_str + character
        else:
            mutated_str = mutated_str + string[index]
    return mutated_str


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
