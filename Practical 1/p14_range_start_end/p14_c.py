#Take two inputs from user called start and end
#Print numbers between those two numbers
#2) Start < print < end
#Example run:start  = 50, end = 53 => print 51,52

start = int(input("Enter start number "))
end = int(input("Enter end number "))

r = range(start, end - 1)
for i in r:
    print(i + 1)