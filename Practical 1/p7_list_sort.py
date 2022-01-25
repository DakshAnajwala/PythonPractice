graphics_cards = []
count = int(input("How many values? "))

for i in range(count):
    gc = int(input(f"Name NVIDIA graphics card no.{i+1} "))
    graphics_cards.append(gc)
graphics_cards.sort()
print(graphics_cards)
#string sort does not consider value of the number
#though integer sort does