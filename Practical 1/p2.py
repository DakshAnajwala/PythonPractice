# what to do:
# take name as input and print the name in uppercase and lowercase
a = input("What is your name? ")

#print(len(a))

print(f"The length of this input is {len(a)}")

#print(a.upper())
print(f"Uppercase version of the input is {a.upper()}")

#print(a.lower())
print(f"Lowercase version of the input is {a.lower()}")

#print(a[2])
print(f"{a[2]} is the third character of input")

if len(a) > 10:
    print(f"{a[10]} is the eleventh character of input")
else:
    print("Insufficient characters")