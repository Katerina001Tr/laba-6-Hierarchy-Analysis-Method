def inMatrix(mat, n):
  for i in range(n):
        for j in range(n):
            if (i == j):
                mat[i][j] = 1 
            if (i < j):
                while mat[i][j] == 0: 
                    temp = input(f"Введите отношение критерия {i+1} к критерию {j+1} ")
                    temp = errorCheck(temp)
                    if  (temp > 9) or (temp < 1): 
                        print('Отношение должно быть целым положительным числом от 1 до 9')
                    else:
                        mat[i][j] = temp
                            for i in range(n):
        for j in range(n):
            if (i > j):
                mat[i][j] = 1/mat[j][i]
    return mat
  def outMatrix(mat, n):
    for i in range(n):
        for j in range(n):
            print("{0:.2f}".format(mat[i][j]), end=" ")
        print()
        def matrixSum(mat, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += mat[i][j]
    return sum
  def koef(mat,n,sum):
    st  = []
    #расчёт суммы отношений для каждого отдельного критерия
    for i in range(n):
        sum1=0
        for j in range(n):
            sum1 += mat[j][i]
        st.append(sum1/sum)
    return st
def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        return -1
    return n

n = 0




