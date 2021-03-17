from math import factorial
num = int(input())

for i in range(num):
    n, k = map(int, input().split())
    print(factorial(k)//(factorial(n)*factorial(k-n)))