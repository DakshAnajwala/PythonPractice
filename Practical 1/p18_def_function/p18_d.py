# take a list of dividends and a divisor from user
# print a dictionary with dividend & remainder
# Example input:
# list of numbers = [7,11,17]
# divisor = 5
# result = {7: 2, 11:1, 17:2}

def str_list_2_int_list(str_list):
    int_list = []
    for s in str_list:
        i = int(s)
        int_list.append(i)

    return int_list


def find_remainders(dividend_list, divisor):
    remainder_dict = {}
    for i in dividend_list:
        result = i % divisor
        remainder_dict[i] = result

    return remainder_dict


if __name__ == "__main__":
    inp = input("Enter a list of comma separated numbers ")
    divisor = input("Enter Divisor ")
    divisor = int(divisor)
    inp = inp.split(",")
    int_list = str_list_2_int_list(inp)
    result = find_remainders(dividend_list=int_list, divisor=divisor)
    print(result)
