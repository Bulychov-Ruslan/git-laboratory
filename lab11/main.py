# import random
# import matplotlib.pyplot as plt

# # Генерируем 100 случайных чисел
# random_numbers = [random.randint(1, 100) for i in range(10)]

# # Строим гистограмму распределения случайных чисел
# plt.hist(random_numbers, bins=10)
# plt.title('Гистограмма распределения случайных чисел')
# plt.xlabel('Значения')
# plt.ylabel('Частота')


# res = ' '.join(map(str, random_numbers))
# # Выводим основные статистические характеристики распределения
# print(random_numbers)
# print(f'Среднее значение: {sum(random_numbers)/len(random_numbers)}')
# print(f'Медиана: {sorted(random_numbers)[len(random_numbers)//2]}')
# print(f'Стандартное отклонение: {res}')
# print(f'Минимальное значение: {min(random_numbers)}')
# print(f'Максимальное значение: {max(random_numbers)}')

# plt.show()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=400, bg='white')
canvas.pack()


text_styles = {
    'R': {'fill': '#ffffff', 'font': ('Garet', 100,)},
    'U': {'fill': '#ffffff', 'font': ('Garet', 100,)},
    'S': {'fill': '#ffffff', 'font': ('Garet', 100,)},
    'L': {'fill': '#000000', 'font': ('Garet', 100, 'bold')},
    'A': {'fill': '#000000', 'font': ('Garet', 100, 'bold')},
    'N': {'fill': '#000000', 'font': ('Garet', 100, 'bold')}
}

canvas.create_rectangle(40, 260, 750, 40,  outline="#000000", width=5)
canvas.create_rectangle(60, 240, 400, 60,  fill="#000000", outline="#000000")
canvas.create_text(140, 150, text='R', **text_styles['R'])
canvas.create_text(240, 150, text='U', **text_styles['U'])
canvas.create_text(330, 150, text='S', **text_styles['S'])
canvas.create_text(470, 150, text='L', **text_styles['L'])
canvas.create_text(560, 150, text='A', **text_styles['A'])
canvas.create_text(650, 150, text='N', **text_styles['N'])


root.mainloop()


