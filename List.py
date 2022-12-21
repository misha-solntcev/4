N = int(input())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

for j in range(N-1, -1, -1):
    for i in range(N-1, -1, -1):
        print(a[i][j], end=" ")
    print()
