# # # # -------------------------------1-----------------------------------
# def func(resume): # Функцияналды функция
#     return my_resume

# def ne_func(resume): # Функционалды емес функция
#     print('Функционалды емес функция: ')
#     print(my_resume, end='\n')


# my_resume = {
#     'first_name': 'Bulychov',
#     'last_name': 'Ruslan',
#     'age': 20,
#     'birth_date': '29-10-2002',
#     'email': 'rusbul02@gmail.com',
#     'phone': '87781134170',
#     'skills': ['Python Django', 'Flutter', 'SQL'],
#     'education': 'Computer Science'
# }

# print('Функционалды функция')
# print(func(my_resume), sep='\n')
# ne_func(my_resume)



# # # # -------------------------------2-----------------------------------
# def return_data():
#     my_list = [1, 2, 3, 4, 5]
#     my_tuple = ('Func_prog', 'RMP', 'WEB')
#     my_dict = {'name': 'Ruslan', 'age': 20, 'city': 'Almaty'}
#     return my_list, my_tuple, my_dict
# my_data = return_data()
# my_list = my_data[0]
# my_tuple = my_data[1]
# my_dict = my_data[2]
# print(my_list)
# print(my_tuple)
# print(my_dict)



# # # # -------------------------------3-----------------------------------
# from functools import reduce

# res = [1, 4, 8, 10, 9, 100]

# print(tuple(map(lambda x: x**2, res)))
# print(tuple(filter(lambda x: x % 2 == 0, res)))
# print(reduce(lambda x, y: x + y, res))



# Функция map применяет заданную функцию к каждому элементу последовательности и возвращает новую последовательность, содержащую результаты.
# Функция filter возвращает новую последовательность, содержащую только те элементы исходной последовательности, для которых функция-аргумент возвращает истинное значение.
# Функция reduce объединяет элементы последовательности посредством заданной функции и возвращает одно значение, которое является результатом сокращения последовательности.


# # # # -------------------------------4-----------------------------------
# def delivery(name, price):
#     del_cost = 0
#     names = ["Аль-Фараби", "Саина", "Ташенова", "Достык"]
#     if name in names:
#         if price < 10000:
#             del_cost = 500
#         else:
#             del_cost = 0
#     else:
#         if price < 10000:
#             del_cost = 1000
#         else:
#             del_cost = 1000
#     return del_cost

# while True:
#     name = input("Көшенің аты: ")
#     price = float(input("Өнім бағасы: "))
#     del_cost = delivery(name, price)
#     print(f"Жеткізу құны: {del_cost} теңге")
#     print()


# # # # -------------------------------5-----------------------------------
# def compose_functions(f, g):
#     def h(x):
#         return f(g(x))
#     return h

# def f(x):
#     return x * 2

# def g(x):
#     return x + 1

# h = compose_functions(f, g)
# print(h(3)) # Выводит 8: f(g(3)) = f(4) = 8
