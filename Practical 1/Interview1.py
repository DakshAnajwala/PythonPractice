# for each query,count how many times each string is occurring in this list


from collections import Counter
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
result = Counter(queries)
print(result)