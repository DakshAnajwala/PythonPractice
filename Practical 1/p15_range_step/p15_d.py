values = input("Pls Enter comma separated numbers ")
values = values.split(",")
num_values = []

for i in values:
    i = int(i)
    num_values.append(i)

print(num_values)