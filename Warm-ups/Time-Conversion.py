
h,m,s= input().split(':')

suffix = s[-2:]

s = s[:-2]

#print(type(h))
if suffix == 'PM' and h!= '12':
  h = int(h)
  h += 12
  h = str(h)

if suffix == 'AM' and h == '12':
  h = '00'


print(h+':'+m+':'+s)








