def solve(val):
    x = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    n = len(x)
    ans = []

    for i in range(n - 1, -1, -1):
        while (val >= x[i]):
            val = val - x[i]
            ans.append(x[i])

    total = 0
    for i in (x):
        count = 0
        for j in (ans):
            if i == j:
                count = count + 1
        if(count != 0):
            print(i,": " ,count)
            total = total + count
    print("Total: ", total, "\n")


if __name__ == '__main__':
    n = int(input("Enter number of notes you want to convert: "))

    for i in range(n):

        val = int(input("Enter the value : "))

        print("Minimal number of change for", n, ": ")

        solve(val)
