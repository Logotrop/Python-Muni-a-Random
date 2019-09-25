def square(n):
    for row in range(n):
        for column in range(n):
            print("něco")
def square2(n):
    for row in range(n):
        print("#" * n)

def pyramida(n):
    for i in range(n):
        print(" " * 2 *(n-1-i)+ "# " * (2*i + 1))
n = int(input("zadej N:"))


pyramida(n)
input()
exit()
