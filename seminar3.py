#Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# some_list = [int(input()) for _ in range(int(input()))]
# summ = 0
# for i in range(1, len(some_list), 2):
#     summ += some_list[i]
# print(summ


#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# some_list = [int(input()) for _ in range(int(input()))]
# new_list = []
# for i in range(len(some_list) // 2 + len(some_list) % 2):
#     new_list.append(some_list[i] + some_list[len(some_list) - 1 - i])
# print(new_list)   


#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))


#Напишите программу, которая 
# будет преобразовывать десятичное число в двоичное.

# s = ''
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

#Задайте число. Составьте список чисел 
# Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

