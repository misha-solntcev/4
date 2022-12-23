n = int(input())
A = []
for i in range(n):
    A.append([0]*n)

i = 1
x = 0
y = -1
x_d = 0
y_d = 1
l = len(str(n**2))
while i <= n ** 2:
    if 0 <= x+x_d < n and 0 <= y+y_d < n and A[x+x_d][y+y_d] == 0:
        x += x_d
        y += y_d
        A[x][y] = i
        i += 1
    else:
        if x_d == 1:
            x_d = 0
            y_d = 1
        elif y_d == 1:
            y_d = 0
            x_d = -1
        elif x_d == -1:
            x_d = 0
            y_d = -1
        elif y_d == -1:
            y_d = 0
            x_d = 1


for i in A:
    for j in i:
        print(str(j).rjust(l), end=" ")
    print()
