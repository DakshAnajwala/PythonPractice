values = input("Pls Enter Start,End,Step ")
values = values.split(",")

start = int(values[0])

end = int(values[1])

step = int(values[2])


r = range(start, end + 1, step)

for i in r:
    print(i)