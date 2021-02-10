n = int(input())
dp = [[0 for i in range(10)] for j in range(1001)]
for i in range(0, 10):
    dp[1][i] = 1
for i in range(0, 1001):
    dp[i][9] = 1

for i in range(2, 1001):
    for j in range(0, 9):
        dp[i][8 - j] = dp[i - 1][8 - j] + dp[i][9 - j]
print(sum(dp[n]) % 10007)