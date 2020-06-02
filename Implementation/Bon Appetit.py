def bonAppetit(bill, k, b, n):

    total = 0
    print("Item not eaten by Anna: ", bill[k])
    for i in range(n):
        if bill[i] != bill[k]:
            total += bill[i]
        else:
            continue

    b_actual = total / 2

    print(total)
    print(b_actual)
    if b_actual == b:
        print("Bon Appetit")
    else:
        print(int(b - b_actual))

def main():
    n, k = map(int, input("Enter n and k: ").split())
    bill = list(map(int, input().split()[:n]))
    b = int(input())
    bonAppetit(bill, k, b, n)

if __name__ == "__main__":
    main()