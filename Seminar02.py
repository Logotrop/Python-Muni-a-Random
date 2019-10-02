def plusone(a):
    a += 1
    return a

def fibonacci(a,b,c):
    fibonacci = [a,b]
    for I in range(c-2):
        fib = a+b
        a = b
        b = fib
        fibonacci.append(fib)
    return (fibonacci)

def factorial(f):
    if f == 1:
        return 1
    else:
        return (f * factorial(f-1))

def fact_for(f):
    total = 1
    for I in range(1,f+1):
        total = I * total
    return total

def fact_while(f):
    total = 1
    while f>0:
        total = total * f
        f -= 1
    return total



print(plusone(5))
print(fibonacci(1,2,10))
print(factorial(5))
print(fact_for(5))
print(fact_while(5))