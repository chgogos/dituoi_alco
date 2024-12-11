from itertools import permutations


def find_valid_words(letters, dictionary):
    # Δημιουργία όλων των διατάξεων των γραμμάτων
    all_permutations = ["".join(p) for p in permutations(letters)]

    # Εύρεση των έγκυρων λέξεων ελέγχοντας αν υπάρχουν στο λεξικό
    valid_words = [word for word in all_permutations if word in dictionary]

    return valid_words


letters = "cat"
dictionary = ["cat", "act", "dog", "tac", "bat"]

result = find_valid_words(letters, dictionary)

print("Valid words:", result)
