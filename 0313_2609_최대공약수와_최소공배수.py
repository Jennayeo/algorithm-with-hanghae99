a, b = map(int, input().split())
24 18
def find_gcd_lcm(a,b):
    for i in range(1, a+1):1 ~25
        if a % i == 0:
            if b % i == 0:
                gcd=i #for문 다 돌면서 마지막 gcd프린트
    print(gcd)
    if gcd == 1: #최대공약수가 1이라면 서로소
        lcm = a*b
    else:
        lcm = gcd * (a // gcd) * (b // gcd)#최소공배수 구하는 코드
    print(lcm)

find_gcd_lcm(a,b)
