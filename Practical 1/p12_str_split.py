#if 1,2,3 is written, print
#1
#2
#3
num = (input("Enter comma separated numbers "))
nums = num.split(",")
print(nums)

for i in num:
    print(i.strip(","))