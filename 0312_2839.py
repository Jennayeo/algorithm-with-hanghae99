sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar//5) #5로 나눈 몫이 가방 갯수
        print(bag)
        break
    sugar -= 3 #5의 배수가 될때까지 -3해줌
    bag += 1 #-3될때마다 가방 +1
else:
    print('-1')