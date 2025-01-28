import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

def generate_and_count():
    """Генерирует массив случайных чисел и подсчитывает подходящие пары."""
    try:
        arr = [random.randint(-10000, 10000) for _ in range(8)]
        result_text.delete(1.0, tk.END)  # Очищаем текстовое поле

        # Выводим сгенерированный массив
        result_text.insert(tk.END, f"Сгенерированный массив: {arr}\n")

        count = count_pairs(arr) # вызываем функцию подсчета
        result_text.insert(tk.END, f"Количество подходящих пар: {count}\n")

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

def count_pairs(arr):
    """
    Находит количество пар элементов массива, произведение которых нечетно,
    а сумма - положительна.

    Args:
        arr: Массив целых чисел.

    Returns:
        Количество подходящих пар.
    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] * arr[j]) % 2 != 0 and (arr[i] + arr[j]) > 0:
                count += 1
    return count


root = tk.Tk()
root.title("Подсчет пар")

generate_button = tk.Button(root, text="Выполнить", command=generate_and_count)
generate_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(root, width=60, height=10)
result_text.pack()

root.mainloop()
