import math

while True:
  n= int(input())
  if n == 0:
    break
    
  count=0
  
  for i in rage(n+1, 2n+1):
    if i == 1:
      continue
    elif i == 2:
      count += 1
      continue
    else:
      for j in range(2, int(sqrt(i)+1)):
        if i % j = 0:
          break
        else:
          count += 1
          
  print(count)
