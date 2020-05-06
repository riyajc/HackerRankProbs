
sum = 0
y = 0
n = int(input("Array length: ")) #input() stops the execution of the program and reads the line on the console as a string. Type casting int() will convert the input into an integer.
print(type(n))

x = input("Enter values: ").split() #split() function will split the input from the user console after spaces and stores it in an object of type list.
print(type(x)) #

for i in range(n):
  y = int(x[i]) #although x is a list, the elements of the list are of string type. The '+=' will not work with 'str' and 'int'('sum') objects. The list x should be iterated and type casted to 'int' befor adding all the elements.
  sum += y

print(sum)

#for very big numbers 'long long int' might be needed in C/C++ or java as 32-bit 'int' only a range of (-2^31) - (2^31 -1)

