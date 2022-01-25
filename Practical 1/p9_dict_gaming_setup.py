device_price = {}
count = int(input("How many values? "))

for i in range(count):
    device = input("Tell me the name of a device of your gaming setup ")
    cost = int(input("Tell me the cost of a device of your gaming setup "))
    device_price[device] = cost

print(device_price)
