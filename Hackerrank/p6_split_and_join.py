def split_and_join(line):
    # write your code here
    inp = line.split(" ")
    inp = "-".join(inp)
    return inp

if __name__ == '__main__':
    inp = input("Enter Text ")
    inp = split_and_join(inp)
    print(inp)
