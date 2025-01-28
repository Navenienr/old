'''
 на вход программы поступают три целый числа. Необходимо написать программу,
 которая будет вычислять и выводить на экран сумму двух наибольших. Циклические
 операторы использовать не допускается.
'''

number_1 = float (input ("введите первое число"))
number_2 = float (input ("введите второе число"))
number_3 = float (input ("введите третье число"))
if number_1 > number_2:
    number_4 = number_1
else:
    number_4 = number_2
if number_2 > number_3:
    number_5 = number_2
else:
    number_5 = number_3
print (number_5+number_4)