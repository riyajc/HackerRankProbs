x1, v1, x2, v2 = map(int, input().split())



if v1 > v2:
  d = (x2-x1)%(v1-v2)
  if d == 0:
    print("YES")
  else:
    print("NO")
else:
  print("NO")