N = 5


def get_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
        yield sum


gen = get_sum(N)
for i in range(N):
    print(next(gen))
