# import sys
#
# n = int(input())
# dp = [[] for _ in range(n)] # 빈 리스트 만들어줌
# tri = []
#
# for i in range(n):
#     tri.append(list(map(int, sys.stdin.readline().split())))
#     for j in range(tri):
#         if i == 0: #1번 라인은 현재 숫자(7) 그대로 넣어 줌
#             tri[0] = dp[0]
#         elif i == j:
#             dp[1] = (tri[0] + tri[1][0]), (tri[0] + tri[1][1])
#         else:
#             dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + hdddd

n = int(input()) #5
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split()))) #input값 받음
for y in range(1,n): #n=5 #1.y=1 2.y=2, 3.
    for x in range(y+1): #i=1, i+1이될때까지 이 for문 반복 #j=0 #i+1=2 j=0 #i+1=3,j=1
        if x == 0: #7
            tri[y][x] = tri[y][x] + tri[y - 1][x] #7+3, 두번재 반복에서 7+8
        elif y == x: #
            tri[y][x] = tri[y][x] + tri[y - 1][x - 1]
        else: #y=2
            tri[y][x] = max(tri[y - 1][x - 1], tri[y - 1][x]) + tri[y][x]

print(max(tri[n - 1]))