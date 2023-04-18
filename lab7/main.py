# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.update({"color": "White"})
# print('update: ', car)
# print('get: ', car.get("model"))
# print('keys: ', car.keys())
# print('items: ', car.items())
# print('values: ', car.values())


# -------------------------------------1------------------------------------------
# rivers = {
#     "Ніл": "Египет",
#     "Жайық": "Қазақстан",
#     "Сырдария": "Қазақстан",
# }

# print(rivers)

# river = input()
# if river in rivers:
#     print(f"{river} өзен {(rivers[river])} ағып өтеді")
# else:
#     print(f"{river} бұндай өзен жоқ")

# new_country, new_river = input().split()
# rivers.update({new_country: new_river})

# print(rivers)


# # -------------------------------------2------------------------------------------
# result = {}
# while True:
#     comment = input()
#     if comment == '':
#         break
#     name, text = comment.split(': ')
#     if name in result:
#         result[name] += 1
#     else:
#         result[name] = 1
# print(result)
# print(len(result))



# # -------------------------------------3------------------------------------------
# n = int(input())
# result = {}

# for i in range(n):
#     number, name = input().split()
#     result[name] = number

# print(result)

# name = input()
# if name in result:
#     print(result[name])


# # -------------------------------------4------------------------------------------
n = int(input())
result = {}

for i in range(n):
    name, day, month = input().split()
    if month not in result:
        result[month] = []
    result[month].append(name)

print(result)
requested_month = input()

if requested_month in result:
    print(' '.join(result[requested_month]))
else:
    print()
