def my_max(lst):
    return max(lst)


def my_min(lst):
    return min(lst)


def my_print(lst, x):
    return lst[x - 1]


def nonzero_product(numbers):
    suma = 1
    for I in numbers:
        if I != 0:
            suma *= I
    return suma


def double_all(a):
    for I in range(len(a)):
        a[I] *= 2
    return a


def create_double(a):
    b = []
    for I in a:
        b.append(I * 2)
    return b


def flatten(lists):
    res = []
    for I in lists:
        for J in I:
            res.append(J)
    return res


def karen(strink):
    manager = ""
    for I in range(len(strink)):
        if I % 2 == 0:
            if strink[I].islower():
                manager += strink[I].upper()
            else:
                manager += strink[I]
        else:
            if strink[I].isupper():
                manager += strink[I].lower()
            else:
                manager += strink[I]
    return manager


list1 = [1, 0, 3, 5, 0, 7, 0, 8, 9, 20, 0]
listy = [[1, 4, 6], [7, 9, 0], [2, 4]]
y = 3

mysalarygone = str(input("Zadej co řekla Karen:"))

print(my_max(list1))
print(my_min(list1))
print(my_print(list1, y))
print(nonzero_product(list1))
print(double_all(list1))
print(create_double(list1))
print(flatten(listy))
print(karen(mysalarygone))
