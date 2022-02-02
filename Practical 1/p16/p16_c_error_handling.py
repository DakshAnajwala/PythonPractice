names = {}
inp = input("How many people? ")

if not inp.isnumeric():
    print("DON'T U UNDERSTAND WHAT IS A NUMBER!")
else:
    ppl = int(inp)
    for i in range(ppl):
        name_age = input("Enter name,age(comma separated) ")
        name_age = name_age.split(",")

        if len(name_age) < 2:
            print("DON'T U UNDERSTAND WHAT IS COMMA SEPARATED VALUE!")
        else:
            name = name_age[0]
            age = int(name_age[1])
            names[name] = age
    print(names)