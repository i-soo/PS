words = input().upper()  # 모두 대문자로 변경해 저장
unique_words = list(set(words))  # 입력받은 문자열에서 중복되는 값을 set()을 통해 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x) 	# count() 이용
    cnt_list.append(cnt)  # cnt를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # cnt 최대값이 중복되는 경우
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # cnt 최대값의 인덱스
    print(unique_words[max_index])
