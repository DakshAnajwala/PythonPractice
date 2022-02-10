# take list of numbers (inp) from user
# write a function to return sum of all the numbers
def str_list_2_int_list(str_list):
    result = []
    for s in str_list:
        i = int(s)
        result.append(i)
    return result

def add_nums(int_list):
    sum = 0
    for i in int_list:
        sum = sum + i
    return sum

if __name__ == "__main__":
    inp = input("Enter comma separated numbers ")
    inp = inp.split(",")
    int_list = str_list_2_int_list(inp)
    print(int_list)
    result = add_nums(int_list)
    print(result)