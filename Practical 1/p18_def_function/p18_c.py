# take a list of numbers
# Create a dictionary where key is number of teh list and value is 'odd' or 'even'
# print dictionary

# 1,2,3 ==> {1: 'odd', 2: 'even', 3: 'odd'}

def str_list_2_int_list(str_list):
    int_list = []
    for s in str_list:
        i = int(s)
        int_list.append(i)

    return int_list


def check_odd_even(int_list):
    odd_even_dict = {}
    for i in int_list:
        if i % 2 == 1:
            odd_even_dict.update({i: "Odd"})
        else:
            odd_even_dict.update({i: "Even"})
    return odd_even_dict


if __name__ == "__main__":
    inp = input("Enter comma separated numbers ")
    str_list = inp.split(",")
    int_list = str_list_2_int_list(str_list)
    print(int_list)
    result = check_odd_even(int_list)
    print(result)
