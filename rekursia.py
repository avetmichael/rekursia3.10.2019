def ex_1(n):
    if n == 1:
       return 1
    return ex_1(n - 1) + n
print(ex_1(6))

def ex_7():
    f = open("file.txt")
    arr = f.readline().split(",")
    b = 0
    c = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            b = b + int(arr[i])
            c = c + 1
    print(b / c)
    f.close()
ex_7()
#####
def ex_3():
    f = open("file.txt", "r")
    arr = f.readline().split(",")
    c = int(arr[0])
    for i in arr:
        if c < int(i):
            c = int(i)
    f = open("file.txt", "r")
    arr = f.readline().split(",")
    arr = f.readline().split(",")
    b = int(arr[0])
    for j in arr:
        if b > int(j):
            b = int(j)
    print(b * c)
    f.close()
ex_3()
########
def ex_4():
    f = open("file.txt", "r")
    tox = f.readline()
    print(tox)
    a = 0
    for i in tox:
        if i == "a":
            a = a + 1
    print(a)
    tox = f.readline()
    print(tox)
    b = 0
    for j in tox:
        if j == "z":
            b = b + 1
    print(b)
    tox = f.readline().split(",")
    print(tox)
    c = 0
    for k in tox:
            c = c + 1
    print(c)
    f.close()
ex_4()
######
def ex_5(arr):
    f = open("file.txt", "w")
    c = 0
    for i in arr:
        c = c + int(i)
    f.write(str(c))
    f.close()
ex_5([1, 2, 3, 4])








#f = open("file.txt", "a")
#f.writelines(["13756443\n", "238412\n"])
#f.close()


