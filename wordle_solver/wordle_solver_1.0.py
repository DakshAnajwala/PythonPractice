from english_words import english_words_alpha_set

wordle_words = set()

word_set = english_words_alpha_set
#word_set = {'apple', 'appie', 'alpha', 'rough', 'cough', 'tough'}

for s in word_set:
    if len(s) == 5:
        wordle_words.add(s)

print("*************** GREEN CHARACTERS ***************")
g_0 = input("Enter the 1st green character of the word. ")
g_1 = input("Enter the 2nd green character of the word. ")
g_2 = input("Enter the 3rd green character of the word. ")
g_3 = input("Enter the 4th green character of the word. ")
g_4 = input("Enter the 5th green character of the word. ")




matches = []
for word in wordle_words:
    if (not g_0 or word[0] == g_0) \
            and (not g_1 or word[1] == g_1) \
            and (not g_2 or word[2] == g_2) \
            and (not g_3 or word[3] == g_3) \
            and (not g_4 or word[4] == g_4):
        matches.append(word)

print("*************** YELLOW CHARACTERS ***************")

#matches_y_g = set(matches)
while True:
    y_1 = input("Enter a yellow character of the word. ")
    matches_y_g = set()
    for w in matches:
        if y_1 in w:
            matches_y_g.add(w)
    matches = set(matches_y_g)
    grey_char = input("Enter comma separated grey characters that are not in the wordle. ")
    grey_char = grey_char.split(",")
    # matches_y_g = set()
    for w in matches:
        for gr in grey_char:
            if gr in w and w in matches_y_g:
                matches_y_g.remove(w)
    matches = set(matches_y_g)
    print(matches_y_g)
    if len(matches_y_g) == 1:
        print(f"{matches_y_g} is the Word")
        break








