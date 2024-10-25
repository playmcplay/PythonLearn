def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
        print(result)
n=int(input("Enter a number:"))
fact(n)
    