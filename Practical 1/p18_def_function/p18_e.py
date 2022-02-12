# Take list of prices of gaming setup as input.
# Print a dictionary which says if a price is low, medium or high.
# If price < 50, low
# If 50 < price < 500, medium
# If price > 500, high
# 20,80,1900,300 ==> {20: Low, 80: Medium, 1900: High, 300: Medium}


def str_list_2_int_list(str_list):
    int_list = []
    for s in str_list:
        i = int(s)
        int_list.append(i)
    return int_list

def gc_low_medium_high(int_list):
    gc_dict = {}
    for i in int_list:
        if i <= 50:
            #gc_dict[i] == "Low"
            gc_dict.update({i:"Low"})
        if 50 <= i <= 500:
            #gc_dict[i] == "Medium"
            gc_dict.update({i:"Medium"})
        if i >= 500:
            gc_dict.update({i:"High"})
    return gc_dict

if __name__ == "__main__":
    inp = input("Enter comma separated numbers ")
    inp = inp.split(",")
    int_list = str_list_2_int_list(str_list=inp)
    result = gc_low_medium_high(int_list=int_list)
    print(result)


