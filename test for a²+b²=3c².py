#import sentry_sdk
#sentry_sdk.init("https://f579bdfd186e4263a310d4e6a8c0543e@sentry.io/1759097")
limitn = int(input("Zadej minimum:"))
limitm = int(input("Zadej maximum:"))

def test(n, m):
    result = "Žádný výsledek"
    for a in range(n, m):
        for b in range(n, m):
            for c in range(n, m):
                if pow(a, 2) + pow(b, 2) == 3 * pow(c, 2):
                    result = ("Hodnoty jsou:",a,",",b,",",c)
                    break
                #else:
                    #print(a,",",b,",",c)
    print("Test ukončen pro interval ",n," - ",m)
    return result
    
m = limitn
n = limitn
while limitm>m:
    m += 100
    test(n,m)
