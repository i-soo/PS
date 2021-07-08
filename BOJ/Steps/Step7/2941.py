croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # 해당 알파벳 발견시, 임의의 문자로 대체
print(len(word))
