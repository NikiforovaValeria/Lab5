# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
# сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного
# и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной форме.

# Вариант 5: F(x<2) = 1; F(n) = (-1)^n * (F(n-1)/n! + F(n//5) /(2n)!)

# F(n//5) исправлено на F(n-2)

from timeit import default_timer
import math

# Рекурсивная реализация функции F(n) из условия задачи:
def F_recursive(n):
    # Базовый случай: если n < 2, то F(n) = 1
    if n < 2:
        return 1
    # Вычисляем знак через чётность
    sign = 1 if n % 2 == 0 else -1
    term1 = F_recursive(n - 1) / math.factorial(n)   # F(n-1)/n!
    term2 = F_recursive(n - 2) / math.factorial(2 * n)   # F(n-2)/(2n)!
    # Возвращаем результат с учётом знака: (-1)^n * (F(n-1)/n! + F(n-2) /(2n)!)
    return sign * (term1 + term2)

# Итеративная реализация функции F(n)
def F_iterative(n):
    # Базовый случай: если n < 2, то F(n) = 1
    if n < 2:
        return 1
    # Вычисляем знак через чётность
    sign = 1 if n % 2 == 0 else -1
    # Хранение двух предыдущих значений
    f_prev2 = 1    # F(n-2)
    f_prev1 = 1    # F(n-1)
    # Итеративное вычисление факториалов
    fact_n = 1    # текущее значение i!
    fact_2n = 1   # (2i)!
    for i in range(2, n + 1):
        # Обновляем факториалы
        fact_n *= i   # (i-1)! * i
        fact_2n *= (2 * i - 1) * (2 * i)   # (2(i-1))! * (2i-1)*(2i)
        # Вычисляем текущее значение F(i)
        term1 = f_prev1 / fact_n   # F(n-1)/n!
        term2 = f_prev2 / fact_2n   # F(n-2)/(2n)!
        # Вычисляем текущее значение F(i) с учетом знака: (-1)^n * (F(n-1)/n! + F(n-2) /(2n)!)
        current = sign * (term1 + term2)
        # F(i-2) становится F(i-1), а F(i-1) — новым F(i)
        f_prev2, f_prev1 = f_prev1, current
    return f_prev1

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