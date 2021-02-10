inp = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for x in lst:
    inp = inp.replace(x, 'a')
print(len(inp))