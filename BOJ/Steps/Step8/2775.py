array = [[0 for col in range(15)] for row in range(15)] # 호수별 거주자 수를 담을 이차원 배열

for i in range(15):
    array[i][0] = 1
    array[0][i] = i+1

for i in range(1,15):
    for j in range(1,15):
        array[i][j] = array[i-1][j] + array[i][j-1] # 규칙: 왼쪽 옆집 + 바로 아랫집

t = int(input()) # 테스트 케이스 개수
for i in range(t):
    k = int(input())
    n = int(input())

    print(array[k][n-1])
