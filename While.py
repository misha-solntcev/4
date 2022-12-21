n = int(input())
N = list(map(int, input().split()))

count = 0
for i in range(n-1):
    for j in range(n-1-i):
        if N[j] > N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]
            count += 1

print(*N)
print(count)
