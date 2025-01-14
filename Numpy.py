import numpy as np

# Создание массива чисел
data_array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
sum_array = np.sum(data_array)  # Сумма элементов
mean_array = np.mean(data_array)  # Среднее значение
std_array = np.std(data_array)  # Стандартное отклонение

# Вывод результатов
print(f'Array: {data_array}')
print(f'Sum: {sum_array}')
print(f'Mean: {mean_array}')
print(f'Standard Deviation: {std_array}')