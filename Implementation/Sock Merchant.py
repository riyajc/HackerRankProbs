#set(): method used to convert iterable to sequence of iterable with distinct elements,
# called set. Syntax: set(iterable). Parameters: iterable sequence like list, tuple, dic.
# Returns: empty set, if no element passed else, Non-repeating modified iterable set of passed iterable as arg.

#count(): in-built function to return the no of occurences of substring in a given string.
# Syntax: string.count(substring, start=.., end=..). Parameters: substring(mandatory)->string whose count is
# to be found. start/end(optional)-> starting and ending index of string from where search starts and ends.


def sockMerchant(n, ar):
    print(set(ar))

    ar2 = [ar.count(i) for i in set(ar)]
    print(ar2)
    total = 0
    for i in ar2:
        total += int(i/2)

    print(total)

def main():
    n = int(input("Enter num of socks: "))
    arr = list(map(int, input("Enter array of color socks: ").split()[:n]))
    print(n, ar)

    sockMerchant(n, arr)

if __name__ == "__main__":
    main()



