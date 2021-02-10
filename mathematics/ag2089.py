N = int(input())
sol = ""
if N == 1 or N == 0:
    print("0")
else:
    while N != 1:
        if N % 2 == 0:
            sol = "0" + sol
            N = N // -2
        else:
            sol = "1" + sol
            N = (N - 1) // -2
    print("1" + sol) 