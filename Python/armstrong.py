2# Python program to check an Armstrong number

number = int(input("Enter a number "))
sum = 0
test = number
while test > 0:
   digit = test % 10
   sum += digit ** 3
   test //= 10

# display the result
if number == sum:
   print(number,": Armstrong number")
else:
   print(number,": not Armstrong number")