def isUnique(str):
    CheckIsUnique = []
    isUniqueOrNot = set()
    for char in str:
        counted = str.count(char)
        CheckIsUnique.append(counted)
        if counted == 1:
            isUnique_txt = "This is a unique string"
        else:
            isUnique_txt = "This is not a unique string"
        for i in CheckIsUnique:
                if i > 1:
                    isUnique_txt = "This is not a unique string"
    for _ in range(len(str)):
        isUniqueOrNot.add(isUnique_txt)
    print(isUniqueOrNot)
    return isUniqueOrNot


inp = input("Enter a string ")
result = isUnique(inp)