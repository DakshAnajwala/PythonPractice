names = {}
ppl = int(input("How many people? "))

for i in range(ppl):
    name = input("Enter name ")
    age = int(input("Enter age "))
    names[name] = age
print(names)