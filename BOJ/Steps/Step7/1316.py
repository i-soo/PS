n = int(input())

result = n  # 그룹 단어 개수를 입력받은 전체 단어 개수로 초기화
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1] :
            pass
        elif word[j] in word[j+1:] :
            result -= 1
            break
print(result)
