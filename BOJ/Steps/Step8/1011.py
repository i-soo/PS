t = int(input())

for i in range(t) :
    x, y = map(int, input().split())
    
    distance = y - x
    count = 0
    num = 1
    while distance > 0 :
    
        if count % 2 == 1 :
            distance -= num
            num += 1
            count += 1
        else :
            distance -= num
            count += 1
    print(count)  
