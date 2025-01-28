

import tkinter as tk    

from tkinter import ttk
from tkinter import * 
from tkinter import messagebox

window = Tk()
window.title ("calculator")
window.geometry ("400x600") 


#преобразование в числа будет в строку 
#мат операции возвращают, что число ввели до конца и ожиадется ввод нового числа, после этого будет вычисление 


def button_click (str_button):
    
    result_string = str(result_string) + str(str_button)
    print(result_string)

    


label_output_frame = tk.Frame(window,height=100, width=600, bg="green",  )
label_output_frame.place(x=0, y = 0)

label_output = Label(label_output_frame, text = "", wraplength=550, justify="center", font=("Arial",18 ))
label_output.place(x=0, y=0 )

label_button_mas = tk.Frame(window, height=500, width=600, bg="blue",) 
label_button_mas.place(x=0, y=100)

button_1 = tk.Button(label_button_mas, text=1, command = lambda: button_click(1) )
button_1.place(x=50, y=0, width=100, height=100)

button_2 = tk.Button(label_button_mas, text=2, )
button_2.place(x=150, y=0, width=100, height=100)

button_3 = tk.Button(label_button_mas, text=3, )
button_3.place(x=250, y=0, width=100, height=100)

button_4 = tk.Button(label_button_mas, text=4, )
button_4.place(x=50, y=100, width=100, height=100)

button_5 = tk.Button(label_button_mas, text=5, )
button_5.place(x=150, y=100, width=100, height=100)

button_6 = tk.Button(label_button_mas, text=6, )
button_6.place(x=250, y=100, width=100, height=100)

button_7 = tk.Button(label_button_mas, text=7, )
button_7.place(x=50, y=200, width=100, height=100)

button_8 = tk.Button(label_button_mas, text=8, )
button_8.place(x=150, y=200, width=100, height=100)

button_9 = tk.Button(label_button_mas, text=9, )
button_9.place(x=250, y=200, width=100, height=100)

button_0 = tk.Button(label_button_mas, text=0, )
button_0.place(x=150, y=300, width=100, height=100)



button_plus = tk.Button(label_button_mas, text=("+"), )
button_plus.place(x=50, y=300, width=100, height=100)

button_minus = tk.Button(label_button_mas, text=("-"), )
button_minus.place(x=250, y=300, width=100, height=100)

button_multiply = tk.Button(label_button_mas, text=("*"), )
button_multiply.place(x=50, y=400, width=100, height=100)

button_divide = tk.Button(label_button_mas, text=(":"), )
button_divide.place(x=250, y=400, width=100, height=100)

button_equals = tk.Button(label_button_mas, text=("="), )
button_equals.place(x=150, y=400, width=100, height=100)

window.mainloop()


