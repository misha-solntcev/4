n, m = map(int, input().split())
A = []

for i in range(n):
    A.append(list(map(str, input().split())))

black = ['W', 'G', 'B']
b = 0
color = ['C', 'M', 'Y']
c = 0
for i in range(n):
    for j in range(m):
        if a[i][j] in color:
            c += 1
if c > 0:
    print("#Color")
else:
    print("#Black&White")
