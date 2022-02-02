#take 3 input from user
#start , end and step
##1) Start <= print < end

start = int(input("Enter start number "))
end = int(input("Enter end number "))
step = int(input("Enter the step"))

r = range(start, end, step)

for i in r:
    print(i)