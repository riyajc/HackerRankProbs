def pageCount(n, p):

    if n!=p:

        if p % 2 != 0:
            count = int((p-1)/2)
        else:
            count = int(p/2)

        if n % 2 != 0:
            count2 = int((n-p)/2)
        else:
            count2 = int((n+1-p)/2)

        print(min(count, count2))
    else:
        print(0)

def main():

    n = int(input("Enter value n: "))
    p = int(input("Enter value p: "))

    pageCount(n, p)

if __name__ == "__main__":
    main()