
a_dict = {}
words = []
for a_line in open("words_alpha.txt", "r", encoding="utf8"):
    for a_word in a_line.split():
        words.append(a_word)
        a_sorted_word = "".join(sorted(a_word))
        if a_sorted_word not in a_dict:
            a_dict[a_sorted_word] = [a_word]
        else:
            a_dict[a_sorted_word].append(a_word)

for a_word in words:
    a_sorted_word = "".join(sorted(a_word))
    if len(a_dict[a_sorted_word]) >= 5:
        print(f'Word {a_word} -> {a_dict[a_sorted_word]}')