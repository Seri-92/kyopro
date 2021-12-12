n, m = map(int, input().split())
path = []
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    path.append((a, b))
    graph[a].append(b)

def dfs(n, s, graph):
    seen = [False for _ in range(n)]
    seen[s] = True
    todo =[s]
    while todo:
        v = todo.pop()
        for i in range(len(graph[v])):
            x = graph[v][i]
            if seen[x]:
                continue
            seen[x] = True
            todo.append(x)
    # print(seen)
    ans = 0
    for i in range(n):
        if seen[i]:
            ans += 1
    return ans


ans = 0
for i in range(n):
    ans += dfs(n, i, graph)
print(ans)


    
