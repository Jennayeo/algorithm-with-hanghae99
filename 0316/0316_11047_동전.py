import sys

n, k = map(int, input().split())
cnt = []
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
#print(coin)
for i in reversed(coin):
    # if k/i > 1:
    cnt.append(k//i)
    k = k%i
    # elif k/i == 1:
    #     cnt.append(k//i)

print(sum(cnt))