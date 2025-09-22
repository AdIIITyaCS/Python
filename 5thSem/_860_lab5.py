import tkinter as tk

def button_click(number):
    entry.insert(tk.END, number)

def button_clear():
    entry.delete(0, tk.END)

def button_operation(op):
    global first_num
    first_num = float(entry.get())
    entry.delete(0, tk.END)
    global operation
    operation = op

def button_equal():
    second_num = float(entry.get())
    entry.delete(0, tk.END)
    if operation == '+':
        result = first_num + second_num
    elif operation == '-':
        result = first_num - second_num
    elif operation == '*':
        result = first_num * second_num
    elif operation == '/':
        if second_num == 0:
            result = "Not Defined!!!"
        else:
            result = first_num / second_num
    else:
        result = "Invalid operation"
    entry.insert(0, result)

root = tk.Tk()
root.title("CALCI")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

first_num = 0
operation = ''

for (text, row, col) in buttons:
    if text.isdigit():
        command_function = lambda t=text: button_click(t)
    elif text in "+-*/":
        command_function = lambda t=text: button_operation(t)
    elif text == "=":
        command_function = button_equal
    else:
        command_function = button_clear
    
    button = tk.Button(root, text=text, padx=20, pady=10, command=command_function)
    button.grid(row=row, column=col)

root.mainloop()
