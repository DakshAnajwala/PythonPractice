in_put = input("Pls enter comma separated numbers")
number = in_put.split(",")
print(number)

for i in number:
    print(i.strip(","))