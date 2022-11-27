# def factorial_interative(n):
#     fac=1
#     for i in range(n):
#         fac= fac*(i+1)
#     return fac
# Number= int(input("Enter the number "))
# print("Factorail useing interative method", factorial_interative(Number ))


def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n* factorial_recursive(n-1)
number=int(input("Enter the number "))
print("factorial of the given number is:", factorial_recursive(number))