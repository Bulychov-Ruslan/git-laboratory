# set_a = {1, 2}
# set_b = {30, 40}
# cor_a = ('one', 'two', 'three', 'four')

# set_a.add(4)

# cor_b = ', '.join(cor_a)
# print(set_a)
# print(cor_b)
# set_a.update({2, 4, 6})
# print(set_a)
# set_a.remove(6)
# print(set_a)

# set_c = set_a.union(set_b)
# print(set_c)


# # # #--------------------------------------------------------1-----------------------------------------------------------------
# import random

# def rand(a, b, n):
#     return tuple(random.randint(a, b) for _ in range(n))

# cort1 = rand(0, 5, 5)
# cort2 = rand(-5, 0, 5)

# cort3 = cort1 + cort2

# cort4 = cort3.count(0)

# print(cort1)
# print(cort2)
# print(cort3)
# print("0-дер саны: ", cort4)


# # # #--------------------------------------------------------2-----------------------------------------------------------------
# t = (77, (7.7, (7+7j, ("func prog", ()))))

# print(str(t[0]))
# print(str(t[1][0]))
# print(str(t[1][1][0]))
# print(str(t[1][1][1][0]))
# print(str(t[1][1][1][1]))


# # # #--------------------------------------------------------3-----------------------------------------------------------------
# days = ('Дүйсенбі', 'Сейсенбі', 'Сәрсенбі', 'Бейсенбі', 'Жұма', 'Сенбі', 'Жексенбі')

# rashod = []

# for day in days:
#     a = int(input(f"{day} ------ : "))
#     rashod.append(a)

# print(sum(rashod))


# # # #--------------------------------------------------------4-----------------------------------------------------------------
# names = tuple(input().split(" "))

# for name in names:
#     if "ва" in name:
#         print(name)



# # # #--------------------------------------------------------5-----------------------------------------------------------------

# cyr = ('А','Ә','Б','В','Г','Ғ','В','Е','Ё','Ж','З','И','Й','К', 'Қ','Л','М','Н','Ң','О','Ө','П','Р','С','Т','У','Ұ','Ү','Ф', 'Х', 'Һ','Ц','Ч','Ш','Щ','Ъ','Ы','І','Ь','Э','Ю','Я', 'а','ә','б','в','г','ғ','д','е','ё','ж','з','и','й','к','қ','л','м','н','ң','о','ө','п','р','с','т','у','ұ','ү','ф', 'х', 'һ','ц','ч','ш','щ','ъ','ы','і','ь','э','ю','я')
# lat = ('A','A','B','V','G','G','D','E','Io','J','Z','I','I','K','Q','L','M','N','N','O','O','P','R','S','T','U','U','U','F','H','H','Ts','Ch','Sh','Shch','','Y','I','','E','Iu','Ia', 'a','a','b','v','g','g','d','e','io','j','z','i','i','k','q','l','m','n','n','o','o','p','r','s','t','u','u','u','f','h','h','ts','ch','sh','shch','','y','i','','e','iu','ia')

# replace=dict(zip(cyr, lat))
# text = input()
# latin = ''
# for i in text:
#     if i in replace:
#         latin += replace[i]
# print(latin)
