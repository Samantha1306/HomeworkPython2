# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input('Введите целое число: '))
sum = 0
if n <= 0:
    for i in range(n, 2):
        sum += i
else:
    for i in range(1, n+1):
        sum += i

print (f"Сумма целых чисел от 1 до {n} равна {sum}")