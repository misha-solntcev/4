import random
import time
def pi(n):
    i = 0
    count = 0
    while i < n:
        x = random.random()
        y = random.random()
        if (pow(x, 2) + pow(y, 2)) < 1:
            count += 1
        i += 1
    return 4 * (count / n)

start = time.time()
print(pi(100000000))
end = time.time()

print(f"Время выполнения: {end-start} секунд.")