# from english_words import english_words_lower_alpha_set
# word_set = english_words_lower_alpha_set
from nltk.corpus import words
import nltk

nltk.download('words')
word_set = words.words()

# word_set = {'apple', 'appie', 'alpha', 'rough', 'cough', 'tough'}


def green_filter(word_set, index, character):
    filtered_word_set = set()
    index = int(index)
    for w in word_set:
        index_complex = w.find(character)
        if index_complex == index:
            filtered_word_set.add(w)

    return filtered_word_set


def yellow_filter(word_set, yellow_char):
    filtered_word_set = set()
    for word in word_set:
        if yellow_char in word:
            filtered_word_set.add(word)
    return filtered_word_set


def grey_filter(word_set, grey_char):
    filtered_word_set = set()
    for word in word_set:
        if grey_char not in word:
            filtered_word_set.add(word)
    return filtered_word_set


def not_green_filter(word_set, index, not_green_char):
    filtered_word_set = set()
    index = int(index)
    for word in word_set:
        if word[index] != not_green_char:
            filtered_word_set.add(word)
    return filtered_word_set

wordle_words = set()

for s in word_set:
    if len(s) == 5:
        wordle_words.add(s.lower())

word_set = wordle_words
while len(word_set) > 1:
    print("***** GREEN CHARACTERS *****")
    green_chars = {}
    for i in range(5):
        g_all = input("Enter a green character.(Example ==> 0,a) ")
        if not g_all:
            break
        else:
            g_all = g_all.split(",")
            index = g_all[0]
            character = g_all[1]
            word_set = green_filter(word_set=word_set, index=index, character=character)

    print("***** YELLOW CHARACTERS *****")
    # TODO: DOUBLE CHARACTERS TO BE FIXED/IMPROVED
    y = input("Enter yellow characters(Example ==> abc) ")
    for c in y:
        word_set = yellow_filter(word_set=word_set, yellow_char=c)

    print("***** GREY CHARACTERS *****")
    grey = input("Enter grey characters (Example ==> abcde) ")
    for c in grey:
        word_set = grey_filter(word_set=word_set, grey_char=c)

    print("***** NOT GREEN CHARACTERS *****")
    while True:
        not_green_chars = input("Enter a not green character.(Example ==> 0,a) ")
        if not not_green_chars:
            break
        else:
            not_green_chars = not_green_chars.split(",")
            index = not_green_chars[0]
            character = not_green_chars[1]
            word_set = not_green_filter(word_set=word_set, index=index, not_green_char=character)

    print(word_set)
