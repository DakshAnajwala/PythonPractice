# take string from user
# print whether the string is unique string or not
# unique_string = a string with only unique characters

def is_unique(str):
    is_unique_true_false = True
    st = set()
    for c in str:
        st.add(c)
    if len(str) != len(st):
        is_unique_true_false = False

    return is_unique_true_false

if __name__ == '__main__':
    inp = input("Enter a string ")
    result = is_unique(str=inp)
    print(f"Unique string ==> {result}")

