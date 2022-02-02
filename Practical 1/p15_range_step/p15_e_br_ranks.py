ranks = input("Enter comma separated battle royale ranks ")
num_ranks = []
ranks = ranks.split(",")

for i in ranks:
    i = int(i)
    num_ranks.append(i)

num_ranks.sort(reverse=True)
print(num_ranks)