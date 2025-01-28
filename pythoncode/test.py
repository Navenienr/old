import tkinter as tk

def process_input(event=None):
    """Processes number input, stopping at 0 or 100 entries."""
    try:
        num = int(entry.get())
        entry.delete(0, tk.END)  # Clear the entry
        if num == 0:
            entry.config(state=tk.DISABLED) #Disable entry after 0
            result_label.config(text=f"Ввод завершен. Всего чисел: {len(numbers)}")
            return

        numbers.append(num)
        if len(numbers) >= 100:
            entry.config(state=tk.DISABLED) #Disable after 100 entries
            result_label.config(text=f"Достигнут лимит в 100 чисел.")
            return

        result_label.config(text=f"Введено: {num}. Введено всего чисел: {len(numbers)}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter an integer.")


root = tk.Tk()
root.title("Number Input with Limits")

entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Return>", process_input)
entry.focus_set()


numbers = []  # List to store numbers

result_label = tk.Label(root, text="Введите числа, нажимая Enter после каждого. Ввод завершится после ввода 0 или 100 чисел.")
result_label.pack()

root.mainloop()