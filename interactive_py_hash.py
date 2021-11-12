#%%
hash(42)  # το hash ακεράιου είναι ο ίδιος ακέραιος αριθμός
#%%
hash(3.14)
# %%
hash("arta")
# %%
# Η hash συνάρτηση για τα λεκτικά είναι non-commutative (μη μεταθετική)
print(hash("arta"), hash("aart"))
#%%
hash((1, 2, 3, 4))  # οι πλειάδες γίνονται hash διότι είναι immutable
#%%
print(
    hash((1, 2, 3, 4)), hash((1, 2, 3, 4, 5))
)  # η hash τιμή εξαρτάτατι από το σύνολο του κλειδιού
# %%
try:
    hash([1, 2, 3, 4])  # δεν μπορεί να γίνει hash διότι οι λίστες είναι mutable
except Exception as e:
    print(str(e))
# %%
class Student:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester


s1 = Student("Nikos", 3)
s2 = Student("Nikos", 3)

print(hash(s1), hash(s2))
# %%
# για να γίνονται "σωστά" hash τα αντικείμενα της κλάσης Student θα πρέπει να υλοποιηθούν οι συναρτήσεις __eq__ και __hash__
class Student:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester

    def __eq__(self, o: object):
        return self.name == o.name and self.semester == o.semester

    def __hash__(self):
        return hash((self.name, self.semester))


s1 = Student("Nikos", 3)
s2 = Student("Nikos", 3)
s3 = Student("Niki", 3)

print(hash(s1), hash(s2))
print(hash(s1), hash(s3))
# %%
