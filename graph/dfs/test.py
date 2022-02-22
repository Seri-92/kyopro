G = [[], [2, 3], [1, 4], [1], [2, 5], [4]]

seen = [0] * len(G)
todo = [1]
root = []

seen[1] = 1

while todo:
    v = todo.pop()
    root.append(v)
    for w in G[v]:
        if not seen[w]:
            todo.append(w)
            seen[w] = 1
        root.append(v)

print(root)
