#maximum value of the array sum list

  

#minimum value of the array sum list
def min_max_sum(sum_list):
  maximum = sum_list[0]
  minimum = sum_list[0]
  for i in sum_list:
    if i < minimum:
      minimum = i
  
  for i in sum_list:
    if i > maximum:
      maximum = i
  print(minimum, maximum) 

  

#array sum
def array_sum(arr):
  n = len(arr)
  s = [0] *n

  for i in range(1,n):
    s[0] +=arr[i]
  
  for i in range(n):
    if(i==1):
      pass
    else:
      s[1] += arr[i]
  
  for i in range(n):
    if(i==2):
      pass
    else:
      s[2] += arr[i]
  
  for i in range(n):
    if(i==3):
      pass
    else:
      s[3] += arr[i]
  
  for i in range(n-1):
    s[4] += arr[i]
  
  return s


#input values in array
arr = [int(x) for x in input().split()]
print(array_sum(arr))
min_max_sum(array_sum(arr))