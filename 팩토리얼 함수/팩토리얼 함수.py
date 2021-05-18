def factorial(n):
    fac =1
    for i in range(n,0,-1):
        fac = fac*i
    return fac

a= factorial(20)
print(a)