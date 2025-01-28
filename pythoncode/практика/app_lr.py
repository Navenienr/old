text_lr2_1 = """На вход программы поступают три целый числа. Необходимо написать 
программу, которая будет вычислять и выводить на экран сумму двух наибольших. 
Циклические операторы использовать не допускается."""

text_lr2_2 = """Напишите программу, которая по двум данным натуральным числам а и b, не
 превосходящим 30 000, подсчитывает среднее арифметическое удвоенных натуральных
 чисел на отрезке [а, b] (включая концы отрезка). Программа получает на вход два
 натуральных числа а и b, при этом гарантируется, что числа соответствуют заданным
 условиям. Проверять входные данные на корректность не нужно. Программа должна
 вывести одно число: среднее арифметическое удвоенных натуральных чисел 
 на отрезке [а,b]."""

text_lr2_3 = """  Напишите программу, которая в последовательности натуральных чисел
 определяет сумму чисел, кратных 5. Программа получает на вход количество чисел в
 последовательности, а затем сами числа. В последовательности всегда имеется число,
 кратное 5. Количество чисел не превышает 100. Введённые числа не превышают 300.
 Программа должна вывести одно число- сумму чисел, кратных 5."""

text_lr2_4 = """ Напишите программу, которая в последовательности натуральных чисел
определяет сумму всех чисел, кратных 4 и оканчивающихся на 6. Программа получает на
 вход натуральные числа, количество введенных чисел неизвестно, последовательность
 чисел заканчивается числом 0 (0- признак окончания ввода, не входит в
 последовательность). Количество чисел не превышает 100. Введённые числа не
 превышают 300. Программа должна вывести одно число: сумму всех чисел, кратных 4 и
 оканчивающихся на 6"""

text_lr3_1 = """  Создать строку «Сложившаяся структура организации процветает, как ни в чем не 
бывало». Получить из заданной строки:
1. седьмой символ строки;
2. получить слово «структура» одной операцией;
3. вывести элементы строки со 7 по 9;
4. получить срез последних 7-х элементов;
5. проверить, входят ли строки «процветающий» и «организации» в исходную строку ;
6. создать 3 копии исходной строки;
7. распаковать последовательность в переменные, определить их тип,
8. сделать обратное преобразование из переменных в строку ss.
9. извлеките из нее символы с индексами кратными трем.
10. Измерьте длину вашей строки"""

text_lr3_2 = """  Дан целочисленный массив из 6 элементов. Элементы массива
 могут принимать целые значения от 0 до 100 включительно.
 Напишите программу, позволяющую найти и вывести количество
 пар элементов массива, сумма которых не кратна 6, а произведение
 меньше 1 000. Под парой подразумевается два подряд идущих
 элемента массива."""


import tkinter as tk  
import random  
from tkinter import * 

window = Tk()
window.title ("app for web")
window.geometry ("1000x600") 


def button_click_1():
    def number_input(event = None):
        try:
            num = int(label_enry.get())
            numbers.append(num)
            #print (numbers)
            label_enry.delete(0, tk.END) 
            if len(numbers) == 3:
                Label_uotput_results_lr1.delete(1.0, tk.END)
                if numbers[0] >numbers[1]:
                    number_4 = numbers[0]
                else:
                    number_4 = numbers[1]
                if numbers[1] > numbers[2]:
                    number_5 = numbers[1]
                else:
                    number_5 = numbers[2]
                sum_number = number_4 +number_5
                print (sum_number)

                Label_uotput_results_lr1.insert(1.0, f"сумма наибольших чисел = {sum_number}")
                numbers.clear()                
        
        except ValueError:
            Label_uotput_results_lr1.config(text="error")
        
    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0,text_lr2_1)
    Label_uotput.config(state=tk.DISABLED)

    label_frame_lr1 = tk.Frame(window, height=300, width=800, )
    label_frame_lr1.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr1, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr1 = tk.Text(label_frame_lr1, height=10, width=50,)
    Label_uotput_results_lr1.place(x=200,y=50)

    
def button_click_2():
    def number_input(event = None):
        try:
            
            num = int(label_enry.get())
            numbers.append(num)
            label_enry.delete(0, tk.END) 
            if len(numbers) == 2:
                Label_uotput_results_lr1.delete(1.0, tk.END)
                
                if numbers[0] < numbers[1]:
                    left_border = numbers[0]
                    right_border = numbers[1]+1
                else:
                    left_border = numbers[1]
                    right_border = numbers[0]+1
                my_list = []
                for x in range (left_border, right_border):
                    number_3 = 2*x
                    total = number_3
                    my_list.append(total)
                my_list.append(right_border*2)
                #print (sum(my_list))

                Label_uotput_results_lr1.insert(1.0, f" = {sum(my_list)/(right_border-left_border)}")
                numbers.clear()                
        
        except ValueError:
            Label_uotput_results_lr1.config(text="error")

    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0, text_lr2_2)

    label_frame_lr1 = tk.Frame(window, height=300, width=800,)
    label_frame_lr1.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr1, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr1 = tk.Text(label_frame_lr1, height=10, width=50,)
    Label_uotput_results_lr1.place(x=200,y=50)


def button_click_3():
    def number_input(event = None):
        try: 
            Label_uotput_results_lr1.delete(1.0, tk.END)
            num = int(label_enry.get())
            numbers.append(num)
            label_enry.delete(0, tk.END) 
            if len(numbers) == 2:
                if numbers[0] < numbers[1]:
                    left_border = numbers[0]
                    right_border = numbers[1]+1
                else:
                    left_border = numbers[1]
                    right_border = numbers[0]+1
                
                my_list = []
                for x in range (left_border, right_border):
                    if (x % 5) == 0:
                        my_list.append(x)
                Label_uotput_results_lr1.insert(1.0, sum(my_list))
                my_list.clear()
                numbers.clear()

        except ValueError:
            Label_uotput_results_lr1.config(text="error")

    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0, text_lr2_3)

    label_frame_lr1 = tk.Frame(window, height=300, width=800, )
    label_frame_lr1.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr1, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr1 = tk.Text(label_frame_lr1, height=10, width=50,)
    Label_uotput_results_lr1.place(x=200,y=50)

 
def button_click_4():
    def number_input(event = None):
        
        try:
            Label_uotput_results_lr1.delete(1.0, tk.END)
            num = int(label_enry.get())
            label_enry.delete(0, tk.END) 
            numbers.append(num)
            
            if num == 0:
                for x in numbers:
                    if x % 4 == 0 and x % 10 == 6 and x < 300:
                        total_sum_list.append(x)
                print (sum(numbers))    
                Label_uotput_results_lr1.insert(1.0, f"Сумма подходящих чисел: {sum(total_sum_list)}") 
                numbers.clear()
                sum_list.clear()
                total_sum_list.clear()                
                
            if len(numbers) >= 100:
                for x in sum_list:
                    if x % 4 == 0 and x % 10 == 6:
                        total_sum_list.append(x)
                print (sum(total_sum_list))                
                Label_uotput_results_lr1.insert(1.0, f"сумма подходящих чисел: {sum(total_sum_list)}")
                numbers.clear()
                sum_list.clear()
                total_sum_list.clear()
                return

        except ValueError:
            print("ошибка  ")
            Label_uotput_results_lr1.insert(1.0, "Invalid input. Please enter an integer.")

    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0, text_lr2_4)

    label_frame_lr1 = tk.Frame(window, height=300, width=800,)
    label_frame_lr1.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr1, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr1 = tk.Text(label_frame_lr1, height=10, width=50,)
    Label_uotput_results_lr1.place(x=200,y=50)


def button_click_5():

    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0, text_lr3_1)

    new_window = tk.Toplevel(window) 
    new_window.title("app for lr (low)")
    new_window.geometry("1605x600")

    Label_uotput_results_lr1 = tk.Text(new_window, height=40, width=200, wrap=WORD)
    Label_uotput_results_lr1.place(x=0, y=0)

# 1
    seventh_char = line[6]
    Label_uotput_results_lr1.insert(1.0, f"1. Седьмой символ: {seventh_char}\n")

# 2
    word_structure = line[12:21]  
    Label_uotput_results_lr1.insert(2.0, f"2. Слово структура: {word_structure}\n")

# 3
    elements_7_9 = line[6:9]
    Label_uotput_results_lr1.insert(3.0, f"3. Элементы с 7 по 9: {elements_7_9}\n")

# 4
    last_seven = line[-7:]
    Label_uotput_results_lr1.insert(4.0,f"4. Последние 7 элементов: {last_seven}\n")

# 5
    contains_protsvet = "процветающий" and "организации" in line
    Label_uotput_results_lr1.insert(5.0,f"5. Содержит 'процветающий': {contains_protsvet}\n")

# 7
    a, b, c = line.split()[:3] # Распаковка первых трех слов
    Label_uotput_results_lr1.insert(7.0,f"7. Распакованные переменные: a={a}, b={b}, c={c}\n")
    Label_uotput_results_lr1.insert(8.0,f"    Типы переменных: type(a)={type(a)}, type(b)={type(b)}, type(c)={type(c)}\n")

# 8
    restored_ss = " ".join([a, b, c])
    Label_uotput_results_lr1.insert(9.0,f"8. Восстановленная строка: {restored_ss}\n")

# 9
    every_third_char = "".join([line[i] for i in range(0, len(line), 3)])
    Label_uotput_results_lr1.insert(10.0,f"9. Каждый третий символ: {every_third_char}\n")

# 10
    string_length = len(line)
    Label_uotput_results_lr1.insert(11.0,f"10. Длина строки: {string_length}\n")


# 6
    #three_copies = line * 3
    Label_uotput_results_lr1.insert(6.0, f"6. Три копии строки:\n {line *3}\n ")

    Label_uotput_results_lr1.config(state=tk.DISABLED)


def button_click_6():
    def number_input (event = None):
        try:
            Label_uotput_results_lr1.delete(1.0, tk.END)
            num = int(label_enry.get())
            label_enry.delete(0, tk.END)
            numbers.append(num)
            
            
            if len (numbers)==6:
                if ((numbers[0] + numbers[1])% 6) != 0 and (numbers[0]*numbers[1]) < 1000:
                    Label_uotput_results_lr1.insert(1.1,f" это числа {numbers[0]} и {numbers[1]}")
            
                if ((numbers[1] + numbers[2])% 6) != 0 and (numbers[1]*numbers[2]) < 1000:
                    Label_uotput_results_lr1.insert(2.2,f" это числа {numbers[1]} и {numbers[2]}")
            
                if ((numbers[2] + numbers[3])% 6) != 0 and (numbers[2]*numbers[3]) < 1000:
                    Label_uotput_results_lr1.insert(3.3,f" это числа {numbers[2]} и {numbers[3]}")
            
                if ((numbers[3] + numbers[4])% 6) != 0 and (numbers[3]*numbers[4]) < 1000:
                    Label_uotput_results_lr1.insert(4.4,f" это числа {numbers[3]} и {numbers[4]}")
                
                if ((numbers[4] + numbers[5])% 6) != 0 and (numbers[4]*numbers[5]) < 1000:
                    Label_uotput_results_lr1.insert(5.5,f" это числа {numbers[4]} и {numbers[5]}")
            
        
        except ValueError:
            print("ошибка ")
            Label_uotput_results_lr1.insert(1.0, "Invalid input. Please enter an integer.")
            

    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0, text_lr3_2)

    label_frame_lr1 = tk.Frame(window, height=300, width=800,)
    label_frame_lr1.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr1, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr1 = tk.Text(label_frame_lr1, height=10, width=50,)
    Label_uotput_results_lr1.place(x=200,y=50)

    Label_uotput_results_lr1 = tk.Text(label_frame_lr1, height=10, width=50,)
    Label_uotput_results_lr1.place(x=200,y=50)

numbers = []
sum_list = []
total_sum_list = []
line = "Сложившаяся структура организации процветает, как ни в чем не бывало "
global left_border
global right_border

label_output_text = tk.Frame (window, height=300, width=800, )
label_output_text.place(x=200, y=0)


Label_button = tk.Frame(window, height=600, width=200,bg = "green")
Label_button.place(x=0, y=0)


Label_uotput = tk.Text(label_output_text, font=("arial", 15), wrap=tk.WORD)
Label_uotput.place(x=0, y=0,width=800, height=300 )


Button_1 = tk.Button(Label_button, text="лр 2 задание 1", command=button_click_1 )
Button_1.place(x=0, y=0,width=200, height=100)

Button_2 = tk.Button(Label_button, text="лр 2 задание 2", command=button_click_2)
Button_2.place(x=0, y=100,width=200, height=100)

Button_3 = tk.Button(Label_button, text="лр 2 задание 3", command=button_click_3)
Button_3.place(x=0, y=200,width=200, height=100)

Button_4 = tk.Button(Label_button, text="лр 2 задание 4", command=button_click_4)
Button_4.place(x=0, y=300,width=200, height=100)

Button_5 = tk.Button(Label_button, text="лр 3 задание 1", command=button_click_5)
Button_5.place(x=0, y=400,width=200, height=100)

Button_6 = tk.Button(Label_button, text="лр 3 задание 2", command=button_click_6)
Button_6.place(x=0, y=500,width=200, height=100)

Label_uotput.insert(1.0, "выберите задание для проверки слева, нажав кнопку")

window.mainloop()