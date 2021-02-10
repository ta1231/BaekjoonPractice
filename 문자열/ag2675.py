tc = int(input())
for i in range(tc):
    mul, arr = map(str, input().split())
    for i in arr:
        print(i*(int(mul)), end = '')
    print()