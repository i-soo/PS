# n과 n의 각 자리수를 더하는 함수 d(n) 정의
def d(n):
    x = 0
    a = list(str(n))
    for v in a:
        x += int(v)
    return n+x

exist_set = set() # 생성자를 가지는 집합
for i in range(1,10000):
    exist_set.add(d(i))
result_set = set(range(1,10000)) - exist_set # 생성자를 가지는 숫자들을 제외시킴
for num in sorted(result_set):
    print(num)
