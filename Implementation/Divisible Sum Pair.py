def divisibleSumPair(n, k, arr):

    count = 0

    for i in range(n):

        x = i+1

        for j in range(x, n):

            total = arr[i] + arr[j]
            r = total % k

            if r == 0:
                count += 1
                print(i, j)
            else:
                continue

    print(count)

def main():
    n, k = map(int, input("Enter n and k: ").split())
    arr = list(map(int, input("Enter numbers: ").split()[:n]))
    divisibleSumPair(n, k, arr)

if __name__ == "__main__":
    main()
