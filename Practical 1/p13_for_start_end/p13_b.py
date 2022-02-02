#Take two inputs from user called start and end
#Print numbers between those two numbers
#2) Start <= print <= end

start = int(input("Enter start number "))
end = int(input("Enter end number "))

r = end - start

for i in range(r + 1):
    print(start + i)