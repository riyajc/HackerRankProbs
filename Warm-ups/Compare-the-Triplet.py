a = [5, 6, 7]
b = [4, 6, 9]

arr = []

for i in range(len(a)):
  if a[i] > b[i]:
    arr[0] = arr[0] + 1
  elif b[i] > a[i]:
    arr[1] = arr[1] + 1
  else:
    continue

print(arr)