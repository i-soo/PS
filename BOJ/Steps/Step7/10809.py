s = input()
position = [-1]*26   # -1로 초기화
 
for i in range(len(s)):
    if position[ord(s[i])-97] != -1:   # 문자 a의 아스키코드 값: 97 
        continue
    else:
        position[ord(s[i])-97] = i    # 문자의 위치 입력
        
for i in range(26):
    print(position[i], end=' ')
