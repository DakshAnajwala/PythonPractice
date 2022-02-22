# take string from user
# print whether the string is unique string or not
# unique_string = a string with only unique characters
def is_unique(str):
    is_unique_str = True
    for c in str:
        repetions = str.count(c)
        if repetions != 1:
            is_unique_str = False

    return is_unique_str


if __name__ == '__main__':
    inp = input("Enter a string ")
    result = is_unique(str=inp)
    print(result)
