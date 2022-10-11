# Program to add n numbers given by user

n = int(input("Enter the number of elements: "))
sum = 0
for i in range(0, n):
    sum += int(input("Enter the number: "))
print("The sum of the numbers is: ", sum)
