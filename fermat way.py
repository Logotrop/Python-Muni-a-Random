import math
prvocisla = [2]
pseudoprime = []
m = 3
n = 10000

#fermat test
for i in range(m,n):
    if int(pow(2, (i-1)) % i) == 1:
        fermat=True
        pseudoprime.append(i)
        print("Candidate for Prime = ",i)

m=0
#n=int(input("Do jakého čísla? "))
while n-100>prvocisla[len(prvocisla)-1]:
    neniprvocislo = False
    I = 0
    #while (neniprvocislo == False) and (len(prvocisla)+1 < I) :
    #    if (m % prvocisla[I]) == 0 :
    #        neniprvocislo = True
    #    I += 1

    for I in range(len(prvocisla)):
        if pseudoprime[m] % 2 == 0:
            m += 1
        if prvocisla[I] > math.sqrt(pseudoprime[m]):
            break
        if neniprvocislo == True:
            break
        else:
            if (pseudoprime[m] % prvocisla[I]) == 0 :
                neniprvocislo = True
    if neniprvocislo == False:
        prvocisla.append(pseudoprime[m])
        print(pseudoprime[m])
    m += 1