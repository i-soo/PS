n=10001

check = [False, False] + [True] * (n-1)
    
for i in range(2, 101):
      if check[i]:
          for j in range(i*i, n+1, i):
              check[j] = False

t = int(input())

for i in range(t):
      n= int(input())
      a = n // 2
      b = a
      while True:
          if check[a] and check[b]:
              print(a, b)
              break
          else:
              A -= 1
              B += 1
