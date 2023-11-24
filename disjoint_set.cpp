#include <iostream>
#include <vector>

class UnionFind {
public:
    UnionFind(int size) : root(size) {
        for (int i = 0; i < size; i++) {
            root[i] = i;
        }
    }

    int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return find(root[x]);
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            root[rootY] = rootX;
        }
    }

private:
    std::vector<int> root;
};

int main() {
    UnionFind uf(10);

    uf.unionSet(1, 2);
    uf.unionSet(2, 3);
    uf.unionSet(4, 5);
    uf.unionSet(6, 7);
    uf.unionSet(7, 8);

    for (int i = 0; i < 10; i++) {
        std::cout << "Αντιπρόσωπος του κόμβου " << i << ": " << uf.find(i) << std::endl;
    }

    return 0;
}
