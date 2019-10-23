from random import randint


def guess_number_human(upper_bound):
    guess = 0
    number = randint(1, upper_bound)
    while guess != number:
        guess = int(input("Zadej číslo: "))
        if guess > number:
            print("Moc vysoké číslo!")
        elif guess < number:
            print("Moc malé číslo!")
    print("Správně! Hledané číslo bylo: " + str(number))


def guess_number_pc(upper_bound):
    lower_bound = 1
    x = -1
    while x != 1:
        #guess = randint(lower_bound, upper_bound)
        guess = int((upper_bound+lower_bound)/2)
        print("Je číslo " + str(guess) + " menší(0) rovno(1) větší(2) než tvoje číslo?")
        x = int(input())
        if x == 0:
            lower_bound = guess+1
        elif x == 2:
            upper_bound = guess-1
    print("Tvoje číslo je " + str(guess))


def guess_number_pc_pc(upper_bound):
    number = randint(1, upper_bound)
    trys = 0
    lower_bound = 1
    guess = int((lower_bound+upper_bound)/2)
    while guess != number:
        guess = int((lower_bound+upper_bound)/2)
        trys += 1
        if guess < number:
            lower_bound = guess
        elif guess > number:
            upper_bound = guess
    print("Číslo bylo " + str(number) + " a chtělo to " + str(trys) + " pokusů.")

def binary_search(needle, haystack):
    lower_bound = 0
    upper_bound = len(haystack)
    look = (lower_bound + upper_bound)//2
    while haystack[look] != needle:
        look = (lower_bound + upper_bound)//2
        if haystack[look] > needle:
            upper_bound = look
        elif haystack[look] < needle:
            lower_bound = look
        if look == lower_bound:
            return "Není v seznamu!"
            break
    return "Je v seznamu na pozici " + str(look) + " " + str(haystack[look])


#guess_number_human(100)
#guess_number_pc(100)
for J in range(50):
    listcisel = []
    for i in range(50):
        listcisel.append(randint(1, 100))
    listcisel.sort()
    print(binary_search(randint(1, 100), listcisel))
