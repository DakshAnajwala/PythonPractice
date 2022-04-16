# https://word.tips/unscramble/_/words-contain/_Y___/length/5/exclude-letters/Sileroutag/include-letters/My/
from english_words import english_words_lower_alpha_set
from nltk.corpus import words
import nltk

nltk.download('words')
word_set = words.words()
all_words = set()
for w in word_set:
    all_words.add(w)

for w in english_words_lower_alpha_set:
    all_words.add(w)
# all_words = english_words_lower_alpha_set.union(words)
wordle_words = set()

for s in all_words:
    if len(s) == 5:
        wordle_words.add(s.lower())

word_set = wordle_words


def start_finder(start, wordle_words):
    start_lst = []
    for s in wordle_words:
        if s.startswith(start):
            start_lst.append(s)
    return start_lst


if __name__ == "__main__":
    while len(word_set) > 1:
        start = input("Enter what your string starts with ")
        start_result = start_finder(start=start, wordle_words=wordle_words)
        print(start_result)
