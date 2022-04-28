N = int(input())


def gen_Bal(num):
    a, b, c = 1, 1, 1
    for i in range(num):
        yield a
        a, b, c = b, c, a + b + c



gen = gen_Bal(N)
for i in range(N):
    print(next(gen), end=' ')
