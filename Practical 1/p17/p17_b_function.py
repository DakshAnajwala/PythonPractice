# take input from user in comma separated values
# ask user how many numbers to add
# Define a function which takes 'inp' and 'sum' as parameters and returns 'result'

inp = input("Enter comma separated numbers ")
inp = inp.split(",")
sum = input("How many numbers to add? ")
sum = int(sum)
nums = []


def convert_list(str_list):
    int_list = []
    for s in str_list:
        i = int(s)
        int_list.append(i)

    return int_list


def add_values(int_list, sum_indexes):
    r = 0
    for i in range(sum_indexes):
        r = r + int_list[i]
    return r


int_list = convert_list(inp)
result = add_values(int_list, sum)
print(result)

# for s in inp:
#     i = int(s)
#     nums.append(i)



