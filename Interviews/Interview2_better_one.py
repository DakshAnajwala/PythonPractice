def isUnique(str):
    for char in str:
        counted = str.count(char)
        if counted > 1:
            return False
    return True


inp = input("Enter a string ")
result = isUnique(inp)
if result:
    print('This is a unique string')
else:
    print('This is not a unique string')