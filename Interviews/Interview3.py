# reverse given input without using reverse function
def ManualReverse(inp):
    reversed_str = ''
    len_of_input = len(inp)
    for i in range(len_of_input):
        i = 0 - i
        char = inp[i]
        reversed_str = reversed_str + char
    reversed_str = reversed_str + reversed_str[0]
    reversed_str = reversed_str[1:]
    return reversed_str


if __name__ == "__main__":
    print("This program is for reversing a string ")
    inp = input("Enter a string ")
    print("***INITIALIZING***")
    print("***PLEASE STANDBY***")
    print("***PROCESSING***")
    result = ManualReverse(inp=inp)
    print(result)
