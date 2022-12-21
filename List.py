N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M-1, -1, -1):
        print(a[i][j], end=" ")
    print()
