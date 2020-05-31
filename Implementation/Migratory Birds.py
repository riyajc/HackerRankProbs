def migratoryBird(arr):
    c = [0] * 5
    #print(type(c), c)
    arr2 = []
    for i in arr:
        if i == 1:
            c[0] += 1

        elif i == 2:
            c[1] += 1
            #print(c[1])

        elif i == 3:
            c[2] += 1

        elif i == 4:
            c[3] += 1

        elif i == 5:
            c[4] += 1

    print(c)
    temp = max(c)
    print("max val:", temp)

    #print("Length of c:", len(c))

    for i in range(5):

        if c[i] == temp:
            arr2.append(i)

    print(arr2)

    temp2 = min(arr2)
    index = temp2 + 1
    print("Output: ", index)


def main():
    n = int(input("Enter n:"))
    print(type(n))
    arr = list(map(int, input().split()))
    print(type(arr), arr)
    migratoryBird(arr)

if __name__ == "__main__":
    main()
