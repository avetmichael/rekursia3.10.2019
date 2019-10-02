import math
arr = ([[1, 15, 8, -12],
        [2, 2, 1, 5],
        [1, 7, 7, -7],
        [11, -18, 4, 1]])
def func_m(func_nam,arg,get):
    if ret == func_nam(arg):
        return True
    return False
def ex_434(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    c = 0
    for i in range(0, n):
        for j in range(n - i - 1, n):
            if math.fabs(arr[i][j]) >= 5.3 and math.fabs(arr[i][j]) <= 15.4:
                c = c + arr[i][j]
            print(arr[i][j], end=" ")
        print()
    return c
print(ex_434(arr))
#########
def ex_436(arr):
    a = 0
    b = 0
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i):
            if arr[i][j] >= 0 and arr[i][j] <= 10:
                a = a + arr[i][j]**2
                b = math.sqrt(a)
            print(arr[i][j], end=" ")
        print()
    return b
print(ex_436(arr))
###########
def ex_437(arr):
    a = 0
    b = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i):
            if arr[i][j] == int(arr[i][j]):
                a = a + arr[i][j] ** 2
                b = math.sqrt(a)
            print(arr[i][j], end=" ")
        print()
    return b
print(ex_437(arr))
###########
def ex_438(arr):
    a = 0
    n = len(arr)
    for i in range(1, n):
        for j in range(0, i):
            if j % 2 == 0 and arr[i][j] > 0:
                a = a + 1
            print(arr[i][j], end=" ")
        print()
    return a
print(ex_438(arr))
###############
def ex_439(arr):
    a = 1
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (i + j) % 2 == 1:
                a = a * arr[i][j]
            print(arr[i][j], end=" ")
        print()
    return a
print(ex_439(arr))
#########
def ex_440(arr):
    a = 0
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (i + j) % 2 == 0:
                a = a + arr[i][j]
            print(arr[i][j], end=" ")
        print()
    return a
print(ex_440(arr))
###########
def ex_441(arr):
    a = 0
    b = 0
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i][j] > 0:
                a = a + arr[i][j]**2
                b = math.sqrt(a)
            print(arr[i][j], end=" ")
        print()
    return b
print(ex_441(arr))
###########
def ex_442(arr):
    a = 0
    b = 0
    c = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i):
            if arr[i][j] < 0:
                a = a + arr[i][j]
                b = b + 1
                c = a / b
            print(arr[i][j], end=" ")
        print()
    return c
print(ex_442(arr))
############
def ex_445(arr):
    a = 0
    k = 9
    n = len(arr)
    for i in range(0, n):
        for j in range(0, i + 1):
            if math.fabs(arr[i][j]) > k:
                a = a + 1
            print(arr[i][j], end=" ")
        print()
    return a
print(ex_445(arr))
##########
def ex_447(arr):
    b = 1
    a = 8
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i):
            if arr[i][j] > a:
                b = b * arr[i][j]
            print(arr[i][j], end=" ")
        print()
    return a
print(ex_447(arr))
#############
def ex_449(arr):
    a = 0
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i -1):
            if int(arr[i][j]) % 4 == 0:
                a = a + arr[i][j]
            print(arr[i][j], end=" ")
        print()
    return a
print(ex_449(arr))
###########
def ex_450(arr):
    a = 0
    b = 20
    n = len(arr)
    for i in range(1, n):
        for j in range(n - i, n):
            if b == 20:
                a = a + (arr[i][j] - arr[i][j] // 1)
            print(arr[i][j], end= " ")
        print()
    return a
print(ex_450(arr))