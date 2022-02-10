# take a list of numbers
# print if odd/even

def str_list_2_int_list(str_list):
    int_list = []
    for s in str_list:
        i = int(s)
        int_list.append(i)

    return int_list


def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    inp = input("Enter comma separated numbers ")
    str_list = inp.split(",")
    int_list = str_list_2_int_list(str_list)
    print(int_list)
    for i in int_list:
        if is_odd(num=i):
            print(f"{i} is an odd number")
        else:
            print(f"{i} is an even number")



