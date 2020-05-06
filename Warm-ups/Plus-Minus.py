n = int(input())



arr = [int(x) for x in input().split()]


#arr = [1,-1,0, 4, -9]
#x = len(arr)
c1 = c2 = c3 = 0
for i in arr:
  if i > 0:
    c1 += 1
    
  elif i < 0:
    c2 += 1
    
  else:
    c3 += 1
    

c1 = c1/n
c2 = c2/n
c3 = c3/n
print("%.6f" % c1)
print("%.6f" % c2)
print("%.6f" % c3)