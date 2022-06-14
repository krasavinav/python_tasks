lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
s = tuple(map(lambda x: tuple(x.split("=")), lst_in))
z = filter(lambda x: int(x[1]) >= 500, s)
print(*[i[0] for i in z], end=' ')
