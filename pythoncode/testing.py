import tkinter as tk

def process_input():
    """Processes the input string, extracts numbers, and performs checks."""
    input_str = entry.get()
    try:
        numbers = [int(x.strip()) for x in input_str.split(',')] #splits by commas, removes whitespace
        if len(numbers) != 3:
            result_label.config(text="Please enter exactly three numbers separated by commas.")
            return
        if len(set(numbers)) != 3: #check if numbers are unique
            result_label.config(text="Please enter three unique numbers.")
            return

        result_label.config(text=f"You entered: {numbers}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter three numbers separated by commas.")


root = tk.Tk()
root.title("Three Number Input")

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Process", command=process_input)
button.pack()

result_label = tk.Label(root, text="")  # Label to display the result
result_label.pack()

root.mainloop()