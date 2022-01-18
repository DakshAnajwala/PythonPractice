ages = []
question = int(input("How many values? "))
for i in range(question):
    a = input("What is your age? ")
    a_int = int(a)
    ages.append(a_int)

for age in ages:
    print(age)

for age in ages:
    print(age * 2)
