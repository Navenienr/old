ss = "Сложившаяся структура организации процветает, как ни в чем не бывало"

# 1. Седьмой символ строки
seventh_char = ss[6]
print(f"1. Седьмой символ: {seventh_char}")

# 2. Слово "структура"
word_structure = ss[12:21]  #Индексы 12-20, 21 - не включительно
print(f"2. Слово структура: {word_structure}")

# 3. Элементы строки с 7 по 9
elements_7_9 = ss[6:9]
print(f"3. Элементы с 7 по 9: {elements_7_9}")

# 4. Срез последних 7 элементов
last_seven = ss[-7:]
print(f"4. Последние 7 элементов: {last_seven}")

# 5. Проверка на вхождение "процветающий"
contains_protsvet = "процветающий" and "организации" in ss
print(f"5. Содержит 'процветающий': {contains_protsvet}")

# 6. Три копии исходной строки
three_copies = ss * 3
print(f"6. Три копии строки:\n{three_copies}")

# 7. Распаковка последовательности и определение типа
a, b, c = ss.split()[:3] # Распаковка первых трех слов
print(f"7. Распакованные переменные: a={a}, b={b}, c={c}")
print(f"    Типы переменных: type(a)={type(a)}, type(b)={type(b)}, type(c)={type(c)}")

# 8. Обратное преобразование
restored_ss = " ".join([a, b, c])
print(f"8. Восстановленная строка: {restored_ss}")

# 9. Символы с индексами, кратными трем
every_third_char = "".join([ss[i] for i in range(0, len(ss), 3)])
print(f"9. Каждый третий символ: {every_third_char}")

# 10. Длина строки
string_length = len(ss)
print(f"10. Длина строки: {string_length}")
