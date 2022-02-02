#Take two inputs from user called start and end
#Print numbers between those two numbers
#1) Start < print <= end
#Example run: start = 50, end = 53, =>51, 52, 53

start = int(input("Enter start number "))
end = int(input("Enter end number "))

r = range(start, end)
for i in r:
    print(i + 1)