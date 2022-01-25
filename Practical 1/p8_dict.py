#u hv to ask 2 things
#ask name and age in for loop and store it in

name_age = {}
count = int(input("How many values? "))

for i in range(count):
    question_name = input("What is your name? ")
    question_age = int(input("What is your age? "))
    name_age[question_name] = question_age

print(name_age)