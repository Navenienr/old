text_lr_2_1 = """   На вход программы поступает трехзначное натуральное число. Необходимо
написать программу, которая будет определять, является ли вторая цифра введенного числа
четной. Если условие выполняется, необходимо вывести на экран сообщение «YES», иначе
вывести сообщение «NO»."""

text_lr_2_2 = """   Напишите программу, которая по двум данным натуральным числам а и b, не
превосходящим 30000, подсчитывает среднее арифметическое натуральных чисел,
уменьшенных на заданное число d, на отрезке [а, b] (включая концы отрезка). Программа
получает на вход два натуральных числа а и b, при этом гарантируется, что числа
соответствуют заданным условиям. Проверять входные данные на корректность не нужно.
Программа должна вывести одно число: среднее арифметическое натуральных чисел,
уменьшенных на заданное число d, на отрезке [а, b]."""

text_lr_2_3 = """   Напишите программу, которая в последовательности натуральных чисел
определяет количество чисел, кратных 6 и оканчивающихся на 4. Программа получает на
вход количество чисел в последовательности, а затем сами числа. Количество чисел не
превышает 1 000. Введённые числа по модулю не превышают 30 000. Программа должна
вывести одно число: количество чисел, кратных 6 и оканчивающихся на 4."""

text_lr_2_4 = """   Напишите программу, которая в последовательности натуральных чисел
вычисляет произведение всех двузначных чисел, кратных 8. Программа получает на вход
натуральные числа, количество введенных чисел неизвестно, последовательность чисел
заканчивается числом () (0) … признак окончания ввода, не входит в последовательность).
Количество чисел не превышает 1 000. Введённые числа не превышают 30 000. Программа
должна вывести одно число: произведение всех двузначных чисел, кратных 8."""

text_lr_3_1 = """   Создать строку «Не следует забывать, что спикеры палаты госдумы
негодуют». Получить из заданной строки:
1. пятнадцатый символ строки;
2. получить слово «спикеры» одной операцией;
3. вывести элементы строки со 15 по 17;
4. получить срез последних 15-х элементов;
5. проверить, входят ли строки «палаты» и «госдума» в исходную
строку;
6. создать 3 копии исходной строки;
7. распаковать последовательность в переменные, определить
их тип,
8. сделать обратное преобразование из переменных в строк ss.
9. извлеките из нее символы с индексами кратными трем.
10. Измерьте длину вашей строки."""

text_lr_3_2 = """   Дан массив, содержащий 8 целых чисел в диапазоне от -1 0000 до 1
0000. Напишите программу , которая находит в этом массиве
количество пар всех элементов массива, произведение которых
нечетно, а сумма – положительна.."""

line = "Не следует забывать, что спикеры палаты госдумы негодуют"

text_lr_3_2 = """  Дан массив, содержащий 8 целых чисел в диапазоне от -1 0000 до 1
0000. Напишите программу , которая находит в этом массиве
количество пар всех элементов массива, произведение которых
нечетно, а сумма – положительна. """


numbers=[]
numbers_lr_2_3=[]
sum_list=[]
total_sum_list=[]
lr_2_4 = 1
number = 1


import tkinter as tk  
import math 
from tkinter import * 
from tkinter import messagebox, scrolledtext
import random


window = Tk()
window.title ("app for web")
window.geometry ("1000x600") 

def button_click_1():
    def number_input(event = None):
        try:
            num = int(label_enry.get())
            label_enry.delete(0, tk.END) 

            if num > 99 and num<1000:
                if (int(num / 10)%2) == 0:
                    Label_uotput_results_lr.delete(1.0, END)
                    Label_uotput_results_lr.insert(1.0,"yes")
                else:
                    Label_uotput_results_lr.delete(1.0,END)
                    Label_uotput_results_lr.insert(1.0,"no")
            else:
                Label_uotput_results_lr.delete(1.0,END)
                Label_uotput_results_lr.insert(1.0, "Введите число, котороже подходит по заданию")     
            
        
        except ValueError:
            Label_uotput_results_lr.config(text="error")
    
    
    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0,text_lr_2_1)
    Label_uotput.config(state=tk.DISABLED)

    label_frame_lr = tk.Frame(window, height=300, width=800, )
    label_frame_lr.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr = tk.Text(label_frame_lr, height=10, width=50,)
    Label_uotput_results_lr.place(x=200,y=50)

def button_click_2():
    def number_input(event = None):
        try:
            num = int(label_enry.get())
            numbers.append(num)
            label_enry.delete(0, tk.END) 
            if len(numbers) == 3:
                Label_uotput_results_lr.delete(1.0, tk.END)
                
                if numbers[0] < numbers[1]:
                    left_border = numbers[0]
                    right_border = numbers[1]+1
                else:
                    left_border = numbers[1]
                    right_border = numbers[0]+1
                my_list = []
                for x in range (left_border, right_border):
                    number_3 = x - numbers[2]
                    total = number_3
                    my_list.append(total)
                my_list.append(right_border*2)

                Label_uotput_results_lr.insert(1.0, f" = {sum(my_list)/(right_border-left_border)}")
                numbers.clear()                
        
        except ValueError:
            Label_uotput_results_lr.config(text="error")



    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0,text_lr_2_2)
    Label_uotput.config(state=tk.DISABLED)

    label_frame_lr = tk.Frame(window, height=300, width=800, )
    label_frame_lr.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr = tk.Text(label_frame_lr, height=10, width=50,)
    Label_uotput_results_lr.place(x=200,y=50)

def button_click_3():
    numbers_lr_2_3=[]
    def number_input(event=None):
        try:
            num = int(label_enry.get())
            label_enry.delete(0, tk.END) 

            if num%6==0 and num%10 == 4 and num<30000:
                numbers_lr_2_3.append(num)
            Label_uotput_results_lr.delete(1.0, END)
            Label_uotput_results_lr.insert(1.0,f"количество чисел, которые подходят под условия: {len(numbers_lr_2_3)}")
            
            
        except ValueError:
            Label_uotput_results_lr.config(text="error")    


    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0,text_lr_2_3)
    Label_uotput.config(state=tk.DISABLED)

    label_frame_lr = tk.Frame(window, height=300, width=800, )
    label_frame_lr.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr = tk.Text(label_frame_lr, height=10, width=50,)
    Label_uotput_results_lr.place(x=200,y=50)

def button_click_4():
    def number_input(event = None):
        try:
            Label_uotput_results_lr.delete(1.0, tk.END)
            num = int(label_enry.get())
            label_enry.delete(0, tk.END) 
            
            if num < 30000:
                numbers.append(num)
            
            if num == 0:
                for x in numbers:
                    if x > 9 and x < 100 and x%8==0:
                        sum_list.append(x)
                print (sum_list) 
                Label_uotput_results_lr.delete(1.0, END)
                Label_uotput_results_lr.insert(1.0, f"произведение всех чисел: {math.prod(sum_list)}" )
                sum_list.clear()
                #print (sum_list)
                numbers.clear()
                #print (numbers)



        except ValueError:
            print("ошибка  ")
            Label_uotput_results_lr.insert(1.0, "Invalid input. Please enter an integer.")
            
    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0,text_lr_2_4)
    Label_uotput.config(state=tk.DISABLED)

    label_frame_lr = tk.Frame(window, height=300, width=800, )
    label_frame_lr.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr, )
    label_enry.place(x=50, y = 50)

    label_enry.bind("<Return>", number_input)

    Label_uotput_results_lr = tk.Text(label_frame_lr, height=10, width=50,)
    Label_uotput_results_lr.place(x=200,y=50)

def button_click_5():

    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0, text_lr_3_1)

    new_window = tk.Toplevel(window) 
    new_window.title("app for lr (low)")
    new_window.geometry("1605x600")

    Label_uotput_results_lr1 = tk.Text(new_window, height=40, width=200, wrap=WORD)
    Label_uotput_results_lr1.place(x=0, y=0)

# 1
    symbol_15 = line[14]
    Label_uotput_results_lr1.insert(1.0, f"1. Пятнадцатый символ: '{symbol_15}\n")

# 2
    word_speakers = line[20:27]  
    Label_uotput_results_lr1.insert(2.0, f"2. Слово 'спикеры': '{word_speakers}\n")

# 3
    elements_15_17 = line[14:17]
    Label_uotput_results_lr1.insert(3.0, f"3. Элементы с 15 по 17: '{elements_15_17}\n")

# 4
    last_15_elements = line[-15:]
    Label_uotput_results_lr1.insert(4.0,f"4. Последние 15 элементов: '{last_15_elements}\n")

# 5
    contains_palaty = "палаты" in line
    contains_gosduma = "госдума" in line
    Label_uotput_results_lr1.insert(5.0,f"5. 'палаты' входит: {contains_palaty}, 'госдума' входит: {contains_gosduma}\n")

# 7
    parts = line.split()
    if len(parts) >= 3:
        a, b, c, *_ = parts  
        Label_uotput_results_lr1.insert(6.0,f"7. Распаковка переменных:")
        Label_uotput_results_lr1.insert(7.0,"   a: '{a}' (тип: {type(a)})")
        Label_uotput_results_lr1.insert(8.0,"   b: '{b}' (тип: {type(b)})")
        Label_uotput_results_lr1.insert(9.0,"   c: '{c}' (тип: {type(c)})")
    else:
        Label_uotput_results_lr1.insert(10.0,"7. Распаковка переменных: строка слишком короткая для распаковки")

# 8
    ss = " ".join(parts)
    Label_uotput_results_lr1.insert(12.0,f"8.  Обратное преобразование в строку: '{ss}\n")

# 9
    every_third_char = "".join([line[i] for i in range(0, len(line), 3)])
    Label_uotput_results_lr1.insert(12.0,f"9. Символы с индексами кратными 3: '{every_third_char}\n")

# 10
    string_length = len(line)
    Label_uotput_results_lr1.insert(11.0,f"10. Длина строки: {string_length}\n")


# 6
    #three_copies = line * 3
    Label_uotput_results_lr1.insert(15.0, f"6. Три копии строки:\n {line *3}\n ")
    Label_uotput_results_lr1.config(state=tk.DISABLED)

def button_click_6():
    
    Label_uotput.config(state=tk.NORMAL)
    Label_uotput.delete(1.0, END)
    Label_uotput.insert(1.0,text_lr_2_1)
    Label_uotput.config(state=tk.DISABLED)

    label_frame_lr = tk.Frame(window, height=300, width=800, )
    label_frame_lr.place(x=200, y=300 )

    label_enry = tk.Entry(label_frame_lr, )
    label_enry.place(x=50, y = 50)

    Label_uotput_results_lr = tk.Text(label_frame_lr, height=10, width=50,)
    Label_uotput_results_lr.place(x=200,y=50)

    try:
        arr = [random.randint(-10000, 10000) for _ in range(8)]
        Label_uotput_results_lr.delete(1.0, tk.END)
        Label_uotput_results_lr.insert(tk.END, f"Сгенерированный массив: {arr}\n")
        count = count_pairs(arr) 
        Label_uotput_results_lr.insert(tk.END, f"Количество подходящих пар: {count}\n")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def count_pairs(arr):

    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] * arr[j]) % 2 != 0 and (arr[i] + arr[j]) > 0:
                count += 1
    return count

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