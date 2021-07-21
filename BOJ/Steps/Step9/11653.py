n = int(input())

num = 2               # 나누는 수
while True:           # 소인수분해
    if n % num is 0:
        print(num)
        n //= num
    elif n is 1:
        break
    else:
        num += 1
