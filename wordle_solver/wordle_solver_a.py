from english_words import english_words_set

WORDLE_SIZE = 5
test_words = ['apple','bapple','capple','dapple','eapple']
# print(english_words_set)
# you have to call english words, then it will come
wordle_words = []
for s in english_words_set:
    if len(s) == WORDLE_SIZE:
        wordle_words.append(s)

c = []
for i in range(WORDLE_SIZE):
    c_inp = input(f"Enter the character no. {i + 1} of the word ")
    c.append(c_inp)
# c_1 = c_1.lower()
result = []

for s in wordle_words:
    for i in range(WORDLE_SIZE):
        if c[i].lower() == s[i].lower():
            result.append(s)

print(result)
print(len(result))