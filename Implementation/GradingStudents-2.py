n = int(input())
grades = []
for i in range(n):

  x = int(input().strip())

  if x >=38:

    if x % 5 > 2:
      while x % 5 != 0:
        x += 1

  grades.append(x)  

for i in grades:
  print(i)
