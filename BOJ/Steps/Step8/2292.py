n = int(input())

current_num = 1  # 벌집 방의 번호, 1개부터 시작
count = 1

while n > current_num :
    current_num += 6 * count  # 벌집 방 번호가 6의 배수로 증가
    count += 1
print(count)
