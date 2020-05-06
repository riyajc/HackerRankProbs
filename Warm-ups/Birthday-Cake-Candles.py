

def nof_candles(arr):
  arr.sort()
  print(arr)
  n = len(arr)
  count = 0
  temp = arr[n-1]
  

  for i in arr:
    if(temp == i): count += 1
  
  return count

n = int(input())
arr = [int(x) for x in input().split()]
print(nof_candles(arr))



