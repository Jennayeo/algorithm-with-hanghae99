import sys
import math

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num = sorted(num)

# 최빈값(mode) 구하기
from collections import Counter
cnt = Counter(num)
mode = cnt.most_common()
#print(mode)

num = sorted(num)
avg = math.trunc(round(((sum(num))/n),0)) #소수 첫째자리 반올림, math.trunc로 소수부분 제거
median = num[(len(num))//2]
length = num[-1] - num[0]

print(avg)
print(median)
# if len(mode) > 1:
#     if mode[0][1] == mode[1][1]:
#         print(mode[1][0])
#     else:
#         print(mode[0][0])
# else:
#     print(mode[0][0])

if len(mode) == 1:
    mode = cnt.most_common()
    print(num[0])
elif mode[0][1] == mode[1][1]:
    mode = cnt.most_common(2)
    print(mode[1][0])
elif len(num) == 1: #4000이 자꾸 안먹힘
    print(num[0])
else:
    print(mode[0][0])
#print(cnt)
#print(mode)
print(length)

# 최빈값 구하기 실패
# max_input = max(num)
# find_mode = [0] * max_input
# for i in num:
#     find_mode[i-1] += 1