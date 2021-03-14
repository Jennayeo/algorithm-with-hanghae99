import sys

# cnt = int(input())
# a = 1
#
# for i in range(cnt):
#     j = list(map(int, sys.stdin.readline().split()))
#     for num in j:
#         a *= num
#         if a == j[0]*j[-1]:
#             break
# print(a)

# cnt = int(input())
# for i in range(cnt):
#      j = list(map(int, sys.stdin.readline().split()))
# print(max(j)*min(j))

import sys
cnt = int(input())
j = list(map(int, sys.stdin.readline().split()))
print(max(j)*min(j))