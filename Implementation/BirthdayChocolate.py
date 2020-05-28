#define global variable variable
count = 0


def bc():
  global count    #to modify global variable inside a fun
  s = c = 0
  j = i
  #print("value of j=", j)
  while c < m:
    s += arr[j]
    c += 1
    j += 1
    
  if s == d:
    count += 1

  #print("s=", s)
  #print("count=", count )


#user input
#array of squares with value of chocolate bar
n = int(input("Enter array length:"))
arr = list(map(int, input().split()))
print(arr)

#day and month
d, m = map(int, input().split())
txt = "d = {} m = {}"
print(txt.format(d,m))
print(type(d))

#range to traverse the array
loop_range = n-m+1
print("Loop range= ", loop_range)

#array with one element then no need of traversing
if n == 1:
  if arr[0] == d:
    print("1")
  else:
    print("0")
else:
  for i in range(loop_range):
    print("zzzz")
    bc()  #fun call to calculate no of birthday chocolate pieces
  print(count)




