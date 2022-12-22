n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(str, input())))
input()
b = []
for i in range(n):
    b.append(list(map(str, input())))

count = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1

print(count)
