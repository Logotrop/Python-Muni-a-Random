import math
import time
start = time.time()

prvocisla = [2]
m = 3
n = 60
#n=int(input("Do jakého čísla? "))
while n>prvocisla[len(prvocisla)-1]:
    neniprvocislo = False
    I = 0
    #while (neniprvocislo == False) and (len(prvocisla)+1 < I) :
    #    if (m % prvocisla[I]) == 0 :
    #        neniprvocislo = True
    #    I += 1
    for I in range(len(prvocisla)):
        if m % 2 == 0:
            m += 1
        if prvocisla[I] > math.sqrt(m):
            break
        if neniprvocislo == True:
            break
        else:
            if (m % prvocisla[I]) == 0 :
                neniprvocislo = True
    if neniprvocislo == False:
        prvocisla.append(m)
        print(m)
    m += 1
print ('It took', time.time()-start, 'seconds.')