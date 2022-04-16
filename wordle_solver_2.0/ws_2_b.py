# https://word.tips/wordle
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


def yellow_filter(yellow_chars, wordle_words):
    y_char_lst = []
    for word in wordle_words:
        for c in yellow_chars:
            if c in word:
                y_char_lst.append(word)
    return y_char_lst


if __name__ == "__main__":
    while len(wordle_words) > 1:
        print("***** YELLOW OR GOOD CHARACTERS *****")
        good_char = input("Enter yellow or good characters. Example ==> qwerty ")

        print("***** GREY OR BAD CHARACTERS *****")
        bad_char = input("Enter bad or grey characters. Example ==> abcd ")

        print("***** EXCELLENT OR GREEN CHARACTERS *****")
        for i in range(5):
            excellent_char = input("Enter excellent or green characters. Example ==> 0,a ")

        y_result = yellow_filter(yellow_chars=good_char,wordle_words=wordle_words)

        


