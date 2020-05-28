
def fallen_apples(apples, s, t, a, m):
  apple_count = 0
  for i in range(m):
    apples[i] += a

    if apples[i] >= s and apples[i] <= t:
      apple_count += 1

  print(apple_count)

def fallen_oranges(oranges, s, t, b, n):
  orange_count = 0
  for i in range(n):
    oranges[i] += b

    if oranges[i] >= s and oranges[i] <= t:
      orange_count += 1

  print(orange_count)



#print("Sam's house distance:")
s, t = map(int, input().split())
#print("Location of Apple and Orange tree:")
a, b = map(int, input().split())
#print("No of Apples and Oranges:")
m, n = map(int, input().split())
#print("Apples thrown at distance:")
apples = [int(x) for x in input().split()]
#print("Oranges thrown at distance:")
oranges = [int(x) for x in input().split()]

fallen_apples(apples, s, t, a, m)
fallen_oranges(oranges, s, t, b, n)






