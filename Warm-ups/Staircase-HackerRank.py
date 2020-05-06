n = int(input())


for i in range(1,n+1):
  h = '#' * i
  offset = n-i
  s = ' ' * offset
  print(s+h)
  
