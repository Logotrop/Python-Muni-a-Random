from random import randint, random
import collections

def turn():
    n = randint(1, 6)
    result = 0
    while n % 2 == 0:
        result += n
        n = randint(1, 6)
    return result


def statistics(count, lower, upper):
    min = randint(lower, upper)
    max = min
    cisla = []
    for I in range(count):
        n = randint(lower, upper)
        cisla.append(n)
        if n > max:
            max = n
        if n < min:
            min = n
    avg = sum(cisla)/2
    print(cisla)
    print("Max = ", max, " Min = ", min)


def dice_freq(count):
    cisla = []
    for I in range(count+1):
        n = randint(1, 6)
        cisla.append(n)
    return collections.Counter(cisla)


def two_dice_freq(count):
    cisla = []
    for I in range(count+1):
        n = randint(1, 6)
        m = randint(1, 6)
        cisla.append(n+m)
    return collections.Counter(cisla)


def coin_flip():
    mince = randint(1, 100)
    return mince < 85


def drunkman_simulator(size, steps):
    cesta = []
    for I in range(1, size+1):
        cesta.append(".")
    drunk = int(len(cesta) / 2)
    cesta[drunk] = "*"
    while steps > 0:
        print("Home ", cesta, " Pub")
        if randint(1, 2) == 1:
            if drunk+1 != size:
                cesta[drunk], cesta[drunk+1] = cesta[drunk+1], cesta[drunk]
                drunk += 1
            else:
                print("Drunk in the pub!")
                break
        else:
            if drunk != 0:
                cesta[drunk], cesta[drunk-1] = cesta[drunk-1], cesta[drunk]
                drunk -= 1
            else:
                print("Drunk got home!")
                break
        steps -= 1
    if steps == 0:
        print("Drunk drunk too much - he sleep now...")



drunkman_simulator(10, 100)
print(coin_flip())
print(two_dice_freq(1000))
print(dice_freq(1000))
statistics(10, 1, 100)

print(turn(), turn(), turn(), turn())
