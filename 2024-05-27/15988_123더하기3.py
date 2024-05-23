"""
15988. 1, 2, 3 더하기 3

dp[k] = k를 1,2,3의 합으로 나타내는 경우의 수

k | dp[k]
---------
1  1
2  (1+1, 2) => 2
3 (1+1+1, 2+1, 1+2, 3) => 4
4 (1+1+1+1, 2+1+1, 1+2+1, 3+1, `1+1`+2, `2`+2, `1`+3) => 7
5 => 13
6 => 24
7 => 44
8 => 81
9 => 149
10 => 274
---

= 1+1+1+1+1
= 2+1+1+1
= 1+2+1+1
= 1+1+2+1
= 1+1+1+2
= 2+2+1
= 2+1+2
= 1+2+2
= 3+1+1
= 1+3+1
= 1+1+3
= 3+2
= 2+3

dp[k] = dp[k-1] + dp[k-2] + dp[k-3]
"""
N = 1_000_000
dp = [1, 2, 4] + [0] * (N-3)

for k in range(3, N):
    dp[k] = (dp[k-1] + dp[k-2] + dp[k-3]) % 1_000_000_009

for _ in range(int(input())):
    n = int(input())
    print(dp[n - 1])

