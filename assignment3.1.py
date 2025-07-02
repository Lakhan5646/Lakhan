def factorial(n):

    if n<2:
        return 1
    else :
        return n*(factorial( n - 1))


num=int(input('Enter a number: '))

if num<0:
    print("factorial is not defined for negative number.")
else:
    print(f"factorial of {num} is {factorial(num)}")


