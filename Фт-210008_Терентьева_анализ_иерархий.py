def inMatrix(mat, n):                                                                    # ввод отношения критериев в матрице
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
    for i in range(n):                                                        #расчет дробей в матрице
        for j in range(n):
            if (i > j):
                mat[i][j] = 1/mat[j][i]
    return mat
def outMatrix(mat, n):                                            #вывод матрицы
    for i in range(n):
        for j in range(n):
            print("{0:.2f}".format(mat[i][j]), end=" ")
        print()
def matrixSum(mat, n):                                     #расчет суммы элементов матрицы
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += mat[i][j]
    return sum

def koef(mat,n,sum):                                                               #расчет весовых коэффициентов
    st  = []
    
    for i in range(n):                                                                #сумма отношений для каждого критерия 
        sum1=0
        for j in range(n):
            sum1 += mat[j][i]
        st.append(sum1/sum)
    return st

def errorCheck(n):                                                #обработка ошибок
    try:
        n = int(n)
    except Exception:
        return -1
    return n

n = 0

while n == 0:                                                                            #ввод кол-ва критериев
    n = input("Введите количество критериев для попарного сравнения: ")
    n = errorCheck(n)
    if (n < 1):
        print("Ошибка ввода - количество критериев должно быть положительным целым числом")
        n = 0
mass = [[0] * n for i in range(n)]                                    #формирование матрицы
mass = inMatrix(mass, n)
print("\nМатрица попарного сравнения: ")
outMatrix(mass, n)
mass_sum = matrixSum(mass, n)
print("\nСумма элементов матрицы: {0:.2f}".format(mass_sum))
koef1 = koef(mass, n, mass_sum)                                  #вывод весовых коэффициентов
koef1.reverse()
print("Весовые коэффициенты:", end=" ")
for elem in koef1:
    print("{0:.2f}".format(elem), end=" ") 
