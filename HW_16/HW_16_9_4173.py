with open('input.txt') as f:
    N, M = map(int, f.readline().split())
    children = [[] for _ in range(N + 1)]
    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parts = list(map(int, f.readline().split()))
        for ch in parts[1:]:
            children[i].append(ch)
            parent[ch] = i
    modifications = []
    for _ in range(M):
        S, F = map(int, f.readline().split())
        modifications.append((S, F))

def subtree_hash(node):
    child_hashes = tuple(subtree_hash(child) for child in children[node])
    return hash((len(children[node]), child_hashes))

seen = dict()
h = subtree_hash(1)
seen[h] = 0

found = False
for mod_num, (S, F) in enumerate(modifications, 1):
    prev_parent = parent[S]
    children[prev_parent].remove(S)
    children[F].append(S)
    parent[S] = F

    h = subtree_hash(1)
    if h in seen:
        print(f"{seen[h]} {mod_num}")
        found = True
        break
    seen[h] = mod_num

if not found:
    print(-1)
