#Take two inputs from user called start and end
#Print numbers between those two numbers
#1) Start <= print < end

start = int(input("Enter start number "))
end = int(input("Enter end number "))

r = range(start, end)
for i in r:
    print(i)
