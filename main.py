import tkinter as tk
from tkinter import messagebox

def perform_operation():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return
        else:
            result = num1 / num2
    else:
        messagebox.showerror("Error", "Invalid operation")
        return

    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Basic Arithmetic Calculator")

operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")
operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.grid(row=2, column=1, padx=5, pady=5)

label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.grid(row=0, column=0, padx=5, pady=5)
label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.grid(row=1, column=0, padx=5, pady=5)
label_operation = tk.Label(root, text="Select operation:")
label_operation.grid(row=2, column=0, padx=5, pady=5)
label_result = tk.Label(root, text="Result:")
label_result.grid(row=4, column=0, padx=5, pady=5)


entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)




calculate_button = tk.Button(root, text="Calculate", command=perform_operation)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
