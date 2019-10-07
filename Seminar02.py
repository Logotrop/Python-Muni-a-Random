import math
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

def Cif_Soucet(f):
    cislo = str(f)
    total = 0
    for I in range(0,len(cislo)):
        total += int(cislo[I])
    return (total)

def Cif_Soucet_N1(f):
    cislo = str(f)
    while len(cislo)>1:
        cislo = str(Cif_Soucet(int(cislo)))
    return int(cislo)

def divisors(f):
    div_num = [1]
    for I in range(2, int(f/2)+1):
        if f % I == 0:
            div_num.append(I)
    div_num.append(f)
    return div_num

def divisor_count(f):
    return len(divisors(f))

def is_prime(f):
    return divisor_count(f) == 2

def prime_less_than(f):
    primes=[]
    for I in range(1, f):
        if is_prime(I):
            primes.append(I)
    return primes

def gimme_this_much_primes(f):
    primes = [2, 3]
    I = primes[len(primes)-1]
    while len(primes) < f:
        I += 2
        if is_prime(I):
            primes.append(I)
    return primes




print(plusone(5))
print(fibonacci(1,2,10))
print(factorial(5))
print(fact_for(5))
print(fact_while(5))
print(Cif_Soucet(99999))
print(Cif_Soucet_N1(99999))
print(divisors(60))
print(divisor_count(60))
print(is_prime(7))
print(prime_less_than(60))
print(gimme_this_much_primes(20))