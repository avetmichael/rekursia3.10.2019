def parz_tiv(n):
    for i in range(2, n):
        if n % i == 0:
            return "parz tiv che"
        return "parz tiv e"
print(parz_tiv(23))
#####
def func(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, n - 1):
            arr[i][j] = 10
            for i in range(n):
                print(arr[i])
            return arr
func([[1, 2, 3],
        [4, 5, 6],
        [1, 2, 3]])
def func(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            arr[1][1] = 8    #es meky chkaraca sirun grem(((((
            arr[1][2] = 8
            arr[2][1] = 8
            arr[2][2] = 8
            for i in range(n):
                print(arr[i])
            return arr
func([[1, 2, 5, 7],
      [3, 4, 5, 6],
      [3, 4, 7, 0],
      [1, 2, 9, 6]])





