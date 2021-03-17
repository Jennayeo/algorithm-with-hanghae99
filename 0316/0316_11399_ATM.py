import sys

n = int(input())
Pi= list(map(int, sys.stdin.readline().split()))
Pi = sorted(Pi)

#print(Pi)
for j in range(1, n):
    Pi[j] = Pi[j] + Pi[j - 1]
print(sum(Pi))