n = int(input())

array = list(map(int, input().split()))


def record(arr, n):
  mini = maxi = arr[0]
  min_count = max_count = 0

  for i in range(1, n):
    if arr[i] < mini:
      mini = arr[i]
      #print("min=",mini)
      min_count += 1
      #print("count = ", min_count)
  
  
    elif arr[i] > maxi:
      maxi = arr[i]
      #print("max=", maxi)
      max_count += 1
      #print("count", max_count)
  
    else:
      continue
  
  print(max_count, min_count)

record(array, n)

  


