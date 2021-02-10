a, b = map(str, input().split())
def rev(arr):
    sol = ''
    for i in range(len(arr)):
        sol = sol + arr[len(arr) - 1 - i]
    return sol
a = int(rev(a))
b = int(rev(b))
print(max(a, b))