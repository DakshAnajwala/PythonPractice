# example : "Hello" ==> 'Helo' in any order
inp = input("Enter a string ")
unq_char_set = set()
for c in inp:
    unq_char_set.add(c)

unq_str = ""
for c in unq_char_set:
    unq_str = unq_str + c

print(unq_str)
