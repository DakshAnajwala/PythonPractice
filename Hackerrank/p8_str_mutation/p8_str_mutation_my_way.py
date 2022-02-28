# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    l = []
    for c in string:
        l.append(c)

    l[position] = character

    mutated_str = ''
    for c in l:
        mutated_str.join(c)
    return mutated_str


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
