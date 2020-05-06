n = int(input())

dig1 = 0
dig2 = 0
diff = 0

#initialize matrix
matrix = [] #matrix = [[]]? #matrix = [][]
print("Enter values:")
#input values in matrix
 #A for loop for row
  
for j in range(n): # A for loop for col
  a = []
  for x in input().split():
    a.append(int(x))
    print(a)
  matrix.append(a)
  



print(matrix)

for i in range(n):
  for j in range(n):
    if i==j:
      dig1 += matrix[i][j]
    
    if i+j == n-1:
      dig2 += matrix[i][j]

print(dig1)
print(dig2)

diff = dig1 - dig2 

if diff < 0:
  diff = -diff
print(diff)

#arr = [[0 for i in range(r)] for j in range(c)]
#print(arr)

#x = [int(x) for x in input().split()]
#print(x)
#print(type(x))
#print(type(x[0]))


#for i in range(r):
  #for j in range(c):
    #arr[i][j] = 

#print(arr)