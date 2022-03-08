# for each query,count how many times each string is occurring in this list
queries_test = [
    'starbucks cupertino',
    'McDonalds',
    'apple park',
    'park ave',
    'park ave']
queries = [
    'starbucks cupertino',
    'McDonalds',
    'apple park',
    'park ave',
    'cupertino ca',
    'Mcdonalds',
    'mcdonalds',
    'Starbucks',
    'starbucks',
    'cupertino Ca',
    'starbucks ca',
    'starbucks Ca',
    'mcdonalds SF',
    'apple park',
    'park ave',
    'cupertino ca  ',
    'starbucks Cupertino',
    'mcdonalds',
    'Apple park',
    'park ave',
    'cupertino ca',
    'starbucks cupertino',
    'mcdonalds',
    'mcdonalds',
    'mcdonalds',
    'Starbucks',
    'apple park',
    'park ave',
    'cupertino ca',
]


def occurrences(queries):
    repetitions = {}
    for s in queries:
        s = s.lower()
        if s not in repetitions:
            repetitions[s] = 1
        else:
            repetitions[s] = repetitions[s] + 1
    #         print(f"{s} is not a unique string")
    # print("The others are unique strings")
    return repetitions


def find_unique(repetitions):
    unique_lst = []
    for k in repetitions:
        if repetitions[k] == 1:
            unique_lst.append(k)

    return unique_lst


result = occurrences(queries=queries)
print(result)
unique_str = find_unique(repetitions=result)
print(f"The unique strings are :{unique_str}")