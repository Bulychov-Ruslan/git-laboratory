import random

ticket = random.sample(list(range(1, 50)), 6)

ticket.sort()

for number in ticket:
    print(number, end=" ")
