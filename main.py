# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
# сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного
# и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме.
# Обязательное требование – минимизация времени выполнения и объема памяти.

# Вариант 5: F(x<2) = 1; F(n) = (-1)^n * (F(n-1)/n! + F(n//5) /(2n)!)

from timeit import default_timer
import math

# Словарь для хранения уже посчитанных значений факториалов
factorial_cache = {}

# Функция для вычисления факториала с кэшированием (оптимизация)
def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    result = math.factorial(n)
    factorial_cache[n] = result
    return result

# Рекурсивная реализация функции F(n) из условия задачи:
def F_recursive(n):
    # Базовый случай: если n < 2, то F(n) = 1
    if n < 2:
        return 1
    # Рекуррентная функция: F(n) = (-1)^n * (F(n-1)/n! + F(n//5) /(2n)!)
    return (-1) ** n * (F_recursive(n - 1) / factorial(n) + F_recursive(n // 5) / factorial(2 * n))

# Итеративная реализация функции F(n)
def F_iterative(n):
    # Базовый случай: если n < 2, то F(n) = 1
    if n < 2:
        return 1
    F = [0] * (n + 1)
    F[0] = 1
    F[1] = 1
    # Вычисляем F(i) от 2 до n по формуле: F(n) = (-1)^n * (F(n-1)/n! + F(n//5) /(2n)!)
    for i in range(2, n + 1):
        F[i] = (-1) ** i * (F[i - 1] / factorial(i) + F[i // 5] / factorial(2 * i))
    return F[n]

# Функция для замера времени выполнения функции
def measure_time(func, *args):
    start_time = default_timer()
    result = func(*args)
    end_time = default_timer()
    return result, end_time - start_time

# Тестирование и сравнение рекурсивного и итерационного подходов
results = []
for n in range(1, 7):
    recursive_result, recursive_time = measure_time(F_recursive, n)
    iterative_result, iterative_time = measure_time(F_iterative, n)
    results.append((n, recursive_result, recursive_time, iterative_result, iterative_time))

# Вывод результатов в табличной форме
print(f"{'n':<5} {'F_rec':<15} {'Time_rec':<15} {'F_iter':<15} {'Time_iter':<15}")
print("-" * 60)
for n, rec_res, rec_time, iter_res, iter_time in results:
    print(f"{n:<5} {rec_res:<15.8f} {rec_time:<15.8f} {iter_res:<15.8f} {iter_time:<15.8f}")