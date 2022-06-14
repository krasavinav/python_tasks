s = map(int, input().split())
z = filter(lambda x: 9 < abs(x) < 100, s)
print(*z)
