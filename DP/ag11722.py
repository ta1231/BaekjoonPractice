import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.reverse()
dp = [0] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))