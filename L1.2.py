# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
#
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!

def task_func1(some_list):
    result = 0
    for number in some_list:
        if (
                number // 10 ** 8 + number % 10 ** 8 // 10 ** 7 + number % 10 ** 7 //
                10 ** 6 + number % 10 ** 6 // 10 ** 5 + number % 10 ** 5 //
                10 ** 4 + number % 10 ** 4 // 10 ** 3 + number % 10 ** 3 //
                10 ** 2 + number % 10 ** 2 // 10 + number % 10 // 1) % 7 == 0:
            result += number
    return result


num_list = []
for number_ in range(1, 1001, 2):
    num_list.append(number_ ** 3)
print(task_func1(num_list))
for index in range(len(num_list)):
    num_list[index] += 17
print(task_func1(num_list))