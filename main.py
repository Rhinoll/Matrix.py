import random

def Sort(matrix):

    sortedMartixUpper = []
    sortedMartixDown = []

    print("\nОтсортированный массив: \n")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j]) % 2 == 0:
                sortedMartixUpper.append(matrix[i][j])
            else:
                sortedMartixDown.append(matrix[i][j])

    sortedMartixUpper.sort() #Сортируем по возрастанию
    sortedMartixDown.sort(reverse=True) #Сортируем по убыванию

    finalSort = sortedMartixUpper + sortedMartixDown #Собираем масссивы
    print(finalSort)

def MatrixRandomCreator(m): #Функция создания случайной матрицы

    matrix = [[random.randrange(0, 100) for y in range(m)] for x in range(m)] #Генерируем матрицу, заполненную случайными числами

    print("\nСлучайно сгенерированная матрица размерами ", m, " x ", m,": \n")

    for g in range(len(matrix)):  #Выводим на экран то, что получилось
        for h in range(len(matrix[g])):
            print(matrix[g][h], end = ' ')
        print() #переход на новую строку

    Sort(matrix) #Вызываем логику программы

def MatrixSelfCreator(m): #Функция создания матрицы вручную

    matrix = []

    print("Вы выбрали размер матрицы ", m, "x", m, " не выходите за них - это остановит программу!\nВведите значения с клавиатуры: \n")

    for i in range(m):
        row = input().split()

        if len(row) > m:
            print("Вы превысили границы, которые сами ввели!")
            exit()

        elif len(row) < m:
            print("Вы недостали границы, которую сами ввели!")
            exit()

        for i in range(len(row)):
            try:
                row[i] = int(row[i])
            except ValueError:
                print("Нужно вводить только целые числа, а не строки или дробные числа!")
                exit()

            if row[i] > 100:
                print("По условию задачи, числа не могут превышать сотни!")
                exit()
            elif row[i] < 1:
                print("По условию задачи, числа не могут быть меньше еденицы!")
                exit()

        matrix.append(row)

    print("Ваша матрица: \n")

    for g in range(len(matrix)): #Выводим на экран то, что получилось
        for h in range(len(matrix[g])):
            print(matrix[g][h], end=' ')
        print()  # переход на новую строку

    Sort(matrix) #Вызываем логику программы

if __name__ == '__main__':

    try:
        m = int(input("Введите число от 2 до 5 - размер матрицы: "))
    except ValueError:
        print("Нужно вводить только целые числа, а не строки или дробные числа!")
        exit()

    if m < 2 or m > 5:
        print("Вы ввели неверное значение, размер матрицы должен соответсвовать диапазону из задания!")
        exit()

    ask = input("Матрица содержит только целые цисла в диапазоне от 1 до 100.\nХотите заполнить матрицу случайно - "
                "введите 'y', если с клавиатуры введите 'n': ")

    if ask == 'y':
        MatrixRandomCreator(m)

    elif ask == 'n':
        MatrixSelfCreator(m)

    else:
        print("Нужно вводить 'y' или 'n', а не числа или другие буквы!")