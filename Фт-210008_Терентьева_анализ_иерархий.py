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


