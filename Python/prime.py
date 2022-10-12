#program to checkk prime number using flag.
number = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if number > 1:
    # check for factors
    for j in range(2, number):
        if (number % j) == 0:
         
            flag = True
       
            break

# check if flag is True
if flag:
    print(number, "is not a prime number")
else:
    print(number, "is a prime number")
