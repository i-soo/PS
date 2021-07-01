n, x = map(int, input().split(" "))
l = list(map(int, input().split(" "))) # 리스트에 입력받은 숫자들 저장
 
for i in range(n):
  if l[i] < x :
    print(l[i], end = " ")
