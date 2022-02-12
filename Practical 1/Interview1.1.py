# for each query,count how many times each string is occurring in this list
def occurrences(queries):
    repetitions = {}
    for s in queries:
        s = s.lower()
        if s not in repetitions:
            repetitions[s] = 1
        else:
            repetitions[s] = repetitions[s] + 1

    return repetitions


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

result = occurrences(queries=queries)
print(result)
