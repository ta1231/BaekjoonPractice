n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
temp = (k - 1) % len(arr)
sol = []
for i in range(n - 1):
    sol.append(arr[temp])
    del(arr[temp])
    temp = (temp + (k - 1)) % len(arr)
print("<", end = '')
for i in sol:
    print("{0}, ".format(i), end = '')
print("{0}>".format(arr[0]))
