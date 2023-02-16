# # # # #-------------------------1--------------------------------------
# students = []

# n = int(input("Адам саны: "))
# for i in range(n):
#     group = input("Тобы: ")
#     name = input("Аты: ")
#     course = input("Пәні: ")
#     students.append({'group': group, 'name': name, 'course': course})
#     print({'group': group,'name': name,'course': course })

# cat = input("sort: ")
# res = sorted(students, key=lambda k: k[f'{cat}'])

# for student in res:
#     print(student['group'], student['name'], student['course'])



# # # #-------------------------2--------------------------------------
# grades = {
#     'Nurbol': {'Func_Prog': 80, 'Analiz_d': 90, 'RMP': 75},
#     'Beknur': {'Func_Prog': 90, 'Analiz_d': 85, 'RMP': 95},
#     'Ruslan': {'Func_Prog': 75, 'Analiz_d': 80, 'RMP': 70},
# }

# name = input("name: ")

# for course, grade in grades[name].items():
#     print(f"{course}: {grade}")


# # # #-------------------------3--------------------------------------
# n = []
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     n.append(num)

# n.sort()
# for i in n:
#     if i != 0:
#         print(i, end=" ")



# # # #-------------------------4--------------------------------------
# n = []
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     n.append(num)

# n.sort(reverse=True)
# for i in n:
#     if i != 0:
#         print(i, end=" ")



# # # #-------------------------5--------------------------------------
# import random

# ticket = random.sample(list(range(1, 50)), 6)

# ticket.sort()

# for number in ticket:
#     print(number, end=" ")


# # # #-------------------------6--------------------------------------

# lst = input().split(" ")
# lst = [num for num in lst]

# if sorted(lst) == lst:
#     print(True)
# else:
#     print(False)


