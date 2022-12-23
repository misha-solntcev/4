n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(input())

count = 0
for i in A:
    if 'S' not in i:
        count += 1

num = 0
for j in range(m):
    chet = 0
    for i in range(n):
        if A[i][j] == 'S':
            chet += 1
    if chet == 0:
        num += 1

print(count)
print(num)
print(count*m + num*n - count*num)
