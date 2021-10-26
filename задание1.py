# Вариант 9 вычислить число сочетаний с помощью рекурсии
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def rec(n, m):
     if n < 0 and m < 0:
         print("Отрицательные аргументы недопустимы")
     elif n < m:
         return 0
     elif n == m or m == 0:
         return 1
     else:
         return rec(n - 1, m) + rec(n - 1, m - 1)


if __name__ == '__main__':
  n = int(input("Введите целое число"))
  m = int(input("Введите целое число"))
  print(rec(n, m))
  print("Проверка", math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))