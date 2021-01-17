adj_matrix = [
    [0,1, 1, 0, 0, 0, 0, 0,0],
    [1, 0, 1, 0, 0, 1, 0,0,0],
    [1, 1, 0, 1, 1, 1, 1,0,0],
    [0, 0, 1, 0, 1,0, 1, 1,0],
    [0, 0, 1, 1, 0,0, 1, 1,0],
    [0, 1, 1, 0, 0, 0, 1,0,1],
    [0, 0, 1, 1, 1, 1, 0,1,1],
    [0, 0, 0, 1, 1, 0, 1,0,0],
    [0, 0, 0, 0, 0, 1, 1,0,0],


]

N = {
    i: set(num for num, j in enumerate(row) if j)
    for i, row in enumerate(adj_matrix)
}

print(N)


# {0: {1, 4}, 1: {0, 2, 4}, 2: {1, 3}, 3: {2, 4, 5}, 4: {0, 1, 3}, 5: {3}}

def BronKerbosch2(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch2(
            P=P.intersection(N[v]), R=R.union([v]), X=X.intersection(N[v]))
        X.add(v)


P = N.keys()
print(list(BronKerbosch2(P)))