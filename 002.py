# http://euler.jakumo.org/problems/view/2.html
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

fn1 = 0
fn2 = 1

n = 10

while n >= 0 :
    fn = (fn - 1) + ( fn - 2 )
    print