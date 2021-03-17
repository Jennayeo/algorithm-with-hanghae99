import sys

n = int(input())
dp = [[0,0,0] for _ in range(n)] #빈 리스트 만들어줌
house = []

for i in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))
    if i == 0: #1번 라인은 현재 가격 그대로 넣어 줌
        dp[0][0], dp[0][1], dp[0][2] = house[0][0], house[0][1], house[0][2]
    else:
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + house[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + house[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + house[i][2]
print(min(dp[n - 1]))
