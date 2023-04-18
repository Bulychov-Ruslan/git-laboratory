# # # -----------------------------------1---------------------------------
# import random

# random_numbers = [random.randint(1, 100) for i in range(10)]
# print("Кездесоқ сандар: ", random_numbers)

# sorted_numbers = sorted(random_numbers)
# print("Сұрыпталған кездесоқ сандар", sorted_numbers)

# min_value = min(sorted_numbers)
# max_value = max(sorted_numbers)
# print("Ең кіші сан: ", min_value)
# print("Ең үлкен сан: ", max_value)

# average_value = sum(sorted_numbers) / len(sorted_numbers)
# print("Орташа мәні: ", average_value)

# filtered_numbers = list(filter(lambda x: x > average_value, sorted_numbers))
# print("Орташа мәннен үлкен сандар", filtered_numbers)

# string_numbers = list(map(str, sorted_numbers))
# print("Жолдар тізімі: ", string_numbers)

# merged_string = ''.join(string_numbers)
# print("Біріктірілген сандар тізбегі: ", merged_string)

# split_string = merged_string.split('0')
# print("Тізімді 0 саны бойынша бөл: ", split_string)

# integer_list = list(map(int, split_string))
# print("Список чисел из подстрок:", integer_list)

# sum_of_numbers = sum(integer_list)
# print("0 саны бойынша бөлінген тізім суммасы: ", sum_of_numbers)


# # -----------------------------------2.1-------------------------------
# string = input("Жол енгіз: ")
# res = sorted(set(string))
# print("Бірегей символдар:", res)


# -----------------------------------2.2-------------------------------
# numbers = [2, 4, 6, 8, 10, 11, 12]

# print("Any: ")
# if any(num % 5 == 0 for num in numbers):
#     print("5-ке бөлінетін сандар бар")
# else:
#     print("5-ке бөлінетін сандар жоқ")

# print("All: ")
# if all(num > 1 for num in numbers):
#     print("Барлық сандар 1-ден үлкен")
# else:
#     print("Барлық сандар 1-ден үлкен емес")


# -----------------------------------2.3-------------------------------
# def rotate_matrix(matrix):
#     return [list(reversed(row)) for row in zip(*matrix)]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# rotated_matrix = rotate_matrix(matrix)
# print(rotated_matrix)




# -----------------------------------2.4-------------------------------

# def knapsack_dynamic(weights, values, capacity):

#     n = len(weights)
#     dp = [0] * (capacity + 1)

#     for i in range(n):
#         for j in range(capacity, weights[i] - 1, -1):
#             dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

#     return dp[capacity]

# weights = [1, 3, 4, 5]
# values = [1, 4, 5, 7]
# max_weight = 8
# print(knapsack_dynamic(weights, values, max_weight))



# -----------------------------------2.5-------------------------------
def matrix(mat1, mat2, op):
    n_rows = len(matrix1)
    n_cols = len(matrix1[0])
    result = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            if op == '+':
                row.append(matrix1[i][j] + matrix2[i][j])
            elif op == '-':
                row.append(matrix1[i][j] - matrix2[i][j])
            elif op == '*':
                row.append(sum([matrix1[i][k] * matrix2[k][j] for k in range(n_cols)]))
        result.append(row)
    return result


matrix1 = [[1], [3]]
matrix2 = [[5, 6], [4, 6]]
while True:
    sym = input()
    result = matrix(matrix1, matrix2, sym)
    print(result)





