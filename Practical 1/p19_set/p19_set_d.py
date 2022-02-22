# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1


inp = input("Enter a string: ")
# lst_4_count_function = []
# for c in inp:
#     lst_4_count_function.append(c)
rep = -1
for i in range(len(inp)):
    c = inp[i]
    repetitions = inp.count(c)
    if repetitions == 1:
        rep = i
        break

print(rep)



