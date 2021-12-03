#  https://github.com/deehzee/unionfind
from union_find import UnionFind 

friends = [[ 1, 0 ], [ 2, 3 ], [ 1, 2 ], [ 4, 5 ]]

persons = set([item for sublist in friends for item in sublist])

print(persons)


uf = UnionFind(persons)
for e in friends:
    uf.union(e[0], e[1])


print(uf.components())
