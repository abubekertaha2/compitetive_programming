from collections import defaultdict
n, m = map(int, input().split())
positions = defaultdict(list)
for index in range(1, n + 1):
    word = input().strip()
    positions[word].append(index)
for _ in range(m):
    word = input().strip()
    if positions[word]:
        print(' '.join(map(str, positions[word])))
    else:
        print(-1)
# Enter your code here. Read input from STDIN. Print output to STDOUT
