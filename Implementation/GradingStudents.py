grades = []
n = int(input())

for i in range(n):
  grades.append(int(input()))

print(grades)

for i in range(n):
  
  if grades[i] < 38:
    #print(grades[i])
    pass
  else:
    #print(grades[i])
    remainder = grades[i]%5
    #print(remainder)
    diff = 5-remainder
    #print(diff)

    if diff < 3: 
      grades[i] = grades[i]+diff
      #print("Final grade", grades[i])
    else:
      #print("grade is:", grades[i])
      pass

for i in grades:
  print(i)


