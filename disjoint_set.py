class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        return self.find(self.root[x])

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

# Δημιουργία ενός αντικειμένου UnionFind με 10 κόμβους
uf = UnionFind(10)

# Εκτέλεση κάποιων λειτουργιών ένωσης
uf.union(1, 2)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)
uf.union(7, 8)

# Εκτύπωση των αντιπροσώπων κάθε κόμβου
for i in range(10):
    print(f"Αντιπρόσωπος του κόμβου {i}: {uf.find(i)}")
