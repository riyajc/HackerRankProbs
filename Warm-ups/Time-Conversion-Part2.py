#map(): function used to execute a specific function for each item of an iterable. Syntax - map(myfunc, iterables)."myfunc":- required, the function that executes for each item. "iterables":- A sequence/collecction or an iterator object. It returns a map object which is an iterator object. We can iterator through the map object to access the elements. 

#strip(): function that returns a string with leading and trailing characters removed(based on the string passed in the arg.). Syntax - strip(char). "char":- optional, the char string passed in the arg that is removed from the orginal string. If no arg, white spaces at the front and end are removed. 
time = input().strip()
print(type(time), time)

#bool variable created
is_pm = time[-2:] == 'PM'
print(is_pm)

#[]-> is a list literal. It does not unpack elements. Eg: 
#[(1,2,3)]-> [(1,2,3)]. 
#list()-> is a list function call.It returns a list of items. Eg: list((1,2,3))-> [1,2,3]

#created a list of type int of hour, minute and second.
time_list = list(map(int, time[:-2].split(':')))
print(time_list, type(time_list))

# +12 to hour< 12, if PM
if is_pm and time_list[0] < 12:
  time_list[0] += 12

# if h == 12 and AM, hour = 0
if not is_pm and time_list[0] == 12:
  time_list[0] = 0

print(time_list)

#rjust() method: It right aligns the string, using a specified character(space is by default) as to fill character. Syntax - rjust(number, character). "number"-> required, length of the returned string. "character"-> optional, a character to fill the missing space. white space is default character.

#lambda(): is an anonymous fun. It can take any number of arguments but have only one expression. Syntax - lambda arguments: expression. The expression is executed and the result is returned. 
x = list(map(lambda x: str(x).rjust(2,'0'), time_list))
print(x)

#join(): takes all items in an iterable and joins them into a string. A string must be specified as the seperator. Syntax - string.join(iterable). "iterable"-> required. Any iterable object where all the returned values are strings.
y = ':'.join(x)
print(y)


