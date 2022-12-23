n, m = map(int, input().split())
A = []

start = 0
stop = m
step = 1
for i in range(n):
    B = []
    for j in range(start, stop, step):
        B.append(j)
    A.append(B)
    start += m
    stop += m
    if i % 2 == 0:
        start = start - 1
        stop = stop - 1
    else:
        start = start + 1
        stop = stop + 1
    start, stop = stop, start
    step = - step

for i in range(n):
    for j in range(m):
        print(A[i][j], end=" ")
    print()
