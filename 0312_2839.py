kg = int(input())
bag = 0

if kg%5==0:
    print(kg//5)
elif kg%3==0:
    a = ((kg//5) + ((kg % 5)//3))
    b = (kg//3)
    if a > b:
        print(b)
    else:
        if a == int:
            print(a)
        else:
            print(b)
elif kg!=3 and kg<=7:
    print(-1)
else:
    while kg>=0:
        if kg%5 != 0:
            kg-=3 #3씩 빼주면서 5의배수로 만들어 줌
            bag+=1 #설탕가방 +1해줌
            if kg%5==0:
                break
    print(bag+kg//5)