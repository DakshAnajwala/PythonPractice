values = input("Pls Enter comma separated component prices ")
values = values.split(",")
num_values = []
#values.sort()

for i in values:
    i = int(i)
    print(i)
    num_values.append(i)

num_values.sort()

print(num_values)


#    i = int(i)

