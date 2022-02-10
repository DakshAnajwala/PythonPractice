# ask user to enter comma separated prices of gaming setup
# find percentage of each component of gaming setup out of total gaming setup cost
# example: Input == [20,300,1900,80,50] ==> Output == {20: 0.85%,300:12.76%,1900:80.85%,80:3.4%,50:2.1%}
def str_list_2_int_list(str_list):
    int_list = []
    for s in str_list:
        i = int(s)
        int_list.append(i)
    return int_list


def find_percentage(int_list):
    percentage_gs = {}
    sm = 0
    for i in int_list:
        sm = sm + i

    for i in int_list:
        percentage = i/sm * 100
        percentage = str(percentage)
        percentage = percentage + "%"
        percentage_gs[i] = percentage
    return percentage_gs


if __name__ == "__main__":
    inp = input("Enter comma separated prices of gaming setup ")
    inp = inp.split(",")
    int_list = str_list_2_int_list(str_list=inp)
    result = find_percentage(int_list=int_list)
    print(result)
