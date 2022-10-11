# WAP to Bubble Sort given variables in a list.
a = [5, 3, 8, 6, 7, 2]
n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Sorted array is:")
for i in range(n):
    print("%d" %a[i])
    