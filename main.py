# # 1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# from random import Random


# my_text = "лооабвот льльлабв  абв вба  абвьтл льл ждсб о"
# new_list = []
# for word in my_text.split(' '):
#     if 'абв' not in word:
#         new_list.append(word)
# new_my_text =' '.join(new_list)
# print(new_my_text)

# # 2 Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

# # a)
# from random import randint 
# end = 2021
# first = 4
# end -= first
# count = 1
# while (end != 1):
#     second = randint(1,28)
#     first = randint(1, 28)
#     count += 2
#     end -= second - first
# second = 1
# end = end - second
# if end == 0:
#     print("1 ИГРОК ПОБЕДИЛ!")
# elif end > 0:
#     print("2 ИГРОК ПОБЕДИЛ!")


# # 3 Создайте программу для игры в ""Крестики-нолики"".
# from random import randint 

# def my_func(pole, num, pos): # отрисовка нового хода
#     if num == 1:
#         new_str = "  x  "
#     elif num == 2:
#         new_str = "  o  "
        
#     if pos == 1:
#         pole = new_str + pole[5:]
#     elif pos == 2:
#         pole = pole[:6] + new_str + pole[11:]
#     elif pos == 3:
#         pole = pole[:12] + new_str + pole[17:]
#     elif pos == 4:
#         pole = pole[:36] + new_str + pole[41:]
#     elif pos == 5:
#         pole = pole[:42] + new_str + pole[47:]
#     elif pos == 6:
#         pole = pole[:48] + new_str + pole[53:]
#     elif pos == 7:
#         pole = pole[:72] + new_str + pole[77:]
#     elif pos == 8:
#         pole = pole[:78] + new_str + pole[83:]
#     elif pos == 9:
#         pole = pole[:84] + new_str + pole[89:]
#     return pole

# def my_check(pole): # проверка на выигрыш
#     first = "  x  "
#     second = "  o  "
#     if (pole[0:5] == first and pole[6:11] == first and pole[12:17] == first) or (pole[0:5] == second and pole[6:11] == second and pole[12:17] == second):
#         return True
#     elif (pole[36:41] == first and pole[42:47] == first and pole[48:53] == first) or (pole[36:41] == second and pole[42:47] == second and pole[48:53] == second):
#         return True
#     elif (pole[72:77] == first and pole[78:83] == first and pole[84:89] == first) or (pole[72:77] == second and pole[78:83] == second and pole[84:89] == second):
#         return True
#     elif (pole[0:5] == first and pole[36:41] == first and pole[72:77] == first) or (pole[0:5] == second and pole[36:41] == second and pole[72:77] == second):
#         return True
#     elif (pole[6:11] == first and pole[42:47] == first and pole[78:83] == first) or (pole[6:11] == second and pole[42:47] == second and pole[78:83] == second):
#         return True
#     elif (pole[12:17] == first and pole[48:53] == first and pole[84:89] == first) or (pole[12:17] == second and pole[48:53] == second and pole[84:89] == second):
#         return True
#     elif (pole[0:5] == first and pole[42:47] == first and pole[84:89] == first) or (pole[0:5] == second and pole[42:47] == second and pole[84:89] == second):
#         return True
#     elif (pole[12:17] == first and pole[42:47] == first and pole[72:77] == first) or (pole[12:17] == second and pole[42:47] == second and pole[72:77] == second):
#         return True
#     else:
#         return False

# pole = "  1  |  2  |  3  \n-----------------\n  4  |  5  |  6  \n-----------------\n  7  |  8  |  9  " # исходное поле
# my_list = [] # запись позиций ходов

# print(pole)
# print()
# while len(my_list) != 9:
#     print("Ход игрока 1. Выберите позицию от 1 до 9: ")
#     first = int(input())
#     my_list.append(first)
#     pole = my_func(pole, 1, first)
#     print(pole)
#     print()
#     if my_check(pole) == True:
#         print("Игрок 1 выиграл!")
#         break
#     elif len(my_list) == 9:
#         print("Ничья!")
#         break
#     print("Ход компьютера:")
#     flag = False
#     while flag == False:
#         second = randint(1,9)
#         if second not in my_list:
#             my_list.append(second)
#             pole = my_func(pole, 2, second)
#             flag = True
#         print(pole)
#         print()
#     if my_check(pole) == True:
#         print("Компьютер выиграл!")
#         break
#     elif len(my_list) == 9:
#         print("Ничья!")
#         break
    


# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
def rle(old_str):
    output = ""
    i = 0
    while i < len(old_str):
        count = 1
        while i + 1 < len(old_str) and old_str[i] == old_str[i + 1]:
            count = count + 1
            i = i + 1
        # добавляет к результату текущий символ и его количество
        output += str(count) + old_str[i]
        i = i + 1
    with open("output.txt", "w") as fw:
        fw.write(output)
 
with open("input.txt", "r") as fr:
    rle(fr.read())
    