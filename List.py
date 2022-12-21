# N, M = map(int, input().split())
# a = []
# for i in range(5):
#     a.append(list(map(int, input().split())))
N = 3
M = 4
a = [
    [5, 9, 2, 6],
    [6, 2, 4, 3],
    [1, 2, 8, 7]
]

sum_N = []
for i in range(N):
    s_N = 0
    for j in range(M):
        s_N += a[i][j]
    sum_N.append(s_N)
print(sum_N)
sum_M = []
for j in range(M):
    s_M = 0
    for i in range(N):
        s_M += a[i][j]
    sum_M.append(s_M)
print(sum_M)
