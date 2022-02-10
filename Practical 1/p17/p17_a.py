# take input from user in comma separated values
# ask user how many numbers to add
inp = input("Enter comma separated numbers ")
inp = inp.split(",")
sum = input("How many numbers to add? ")
sum = int(sum)
nums = []
result = 0
for s in inp:
    i = int(s)
    nums.append(i)

for i in range(sum):
    result = result + nums[i]

print(result)
