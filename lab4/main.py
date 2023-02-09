# #------------1----------------
# def reverse(s):
#     return s[::-1]
# s = 'Qazaqstan the best'
# print("Сөз соңынан оқылғанда:", reverse(s))


# def reg(s):
#     print("Үлкен әріп:", s.upper())
#     print("Кіші әріп:", s.lower())
# reg('Qazaqstan the best')


# def sanay(s, n):
#     print(f"{n} - {s.count(n)} рет кездеседі")
# sanay('Qazaqstan the best', 'a')


# def title(s):
#     print(f"Әр сөз үлкен әріппен: {s.title()}")
# title('Qazaqstan the best')

# def swapcase(s):
#     print(f"Үлкен әріптер кішіге, кіші әріптер үлкенге: {s.swapcase()}")
# swapcase('Qazaqstan THE best')

# # ------------2----------------
# students = []

# while True:
#     student = input("Студент аты және классы: ")
#     if student == '-':
#         break
#     name, grade = student.split()
#     students.append((name, int(grade)))

# for name, grade in students:
#     print(f"{name} аты студент {grade} класта оқиды.")


# #------------3----------------
# def rep(s):
#     lower_count = 0
#     upper_count = 0

#     for i in s:
#         if i.islower():
#             lower_count += 1
#         elif i.isupper():
#             upper_count += 1

#     if lower_count >= upper_count:
#         return s.lower()
#     else:
#         return s.upper()

# s = input("Сөз енгіз: ")
# print(rep(s))


# #------------4----------------
# while True:
#     a = input("Бірінші сан: ")
#     b = input("Екінші сан: ")
#     if a.isdigit() and b.isdigit():
#         a = int(a)
#         b = int(b)
#         print("Сумма", a + b)
#         break
#     else:
#         print("Қате. Санді енгіз.")
#


