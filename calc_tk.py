import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("320x500")
window.configure(bg='white')

# CONSTANTS
BG_COLOR = 'white'
std_text = tk.StringVar(value="Standard")
top_results_display = tk.StringVar()
bottom_results_display = tk.StringVar(value="0")

# images
menu_img = tk.PhotoImage(file="C:/Projects/Resources/images/menubar.png")
history_img = tk.PhotoImage(file="C:/Projects/Resources/images/history.png")
resize_img = tk.PhotoImage(file="C:/Projects/Resources/images/resize.png")


# FUNCTIONS
def on_enter(event):
    event.widget.config(bg='lightgray')


def on_leave(event):
    event.widget.config(bg='systemButtonFace')


def display_values(val):
    if bottom_results_display.get() == str(0):
        bottom_results_display.set(value="")
        bottom_results_display.set(value=bottom_results_display.get() + val)
        twelve_values()
    else:
        bottom_results_display.set(value=bottom_results_display.get() + val)
        twelve_values()


def twelve_values():
    if len(bottom_results_display.get()) >= 12:
        results_bottom.config(font="Arial 30")


def clear_values():
    top_results_display.set("")
    bottom_results_display.set("0")
    results_bottom.config(font='Arial 35 bold')


def operators(btn_widget):
    top_results_display.set(bottom_results_display.get() + btn_widget['text'])
    results_top.config(font="Arial 15", fg='grey', anchor='e', textvariable=top_results_display)
    bottom_results_display.set(value="0")


def calculate():
    if "=" in top_results_display.get():
        pass
    else:
        top_results_display.set(top_results_display.get() + bottom_results_display.get() + "=")
        equation = top_results_display.get().strip("=")
        try:
            results = eval(equation)
            bottom_results_display.set(results)
        except ZeroDivisionError:
            results_bottom.config(font='Arial 20 bold')
            bottom_results_display.set('Cannot divide by zero')


# FRAME PARENTS
# top frame
top_frame = tk.Frame(window, bg='white')
# top frame widgets
menu_btn = tk.Button(top_frame, image=menu_img, bd=0, bg='white')
menu_btn.pack(side='left', padx=10)

std_label = tk.Label(top_frame, textvariable=std_text, font=("Helvetica", 15, "bold"), bg='white')
std_label.pack(side='left')

resize_btn = tk.Button(top_frame, bg=BG_COLOR, image=resize_img, bd=0)
resize_btn.pack(side='left', padx=20)

history_btn = tk.Button(top_frame, image=history_img, bd=0, bg=BG_COLOR)
history_btn.pack(side='right', padx=(0, 10))

top_frame.pack(fill='x', pady=(5, 0))

# Results Frame
results_frame = tk.Frame(window, height=130, bg=BG_COLOR)
results_top = tk.Label(results_frame, textvariable=top_results_display, anchor='e', bg=BG_COLOR)
results_top.grid(row=0, column=0, sticky='e')
results_bottom = tk.Label(results_frame, textvariable=bottom_results_display, font="Arial 35 bold", anchor='e',
                          bg=BG_COLOR)
results_bottom.grid(row=1, column=0, sticky='e', columnspan=4)
results_frame.pack_propagate(flag=False)

results_frame.columnconfigure(0, weight=1)
results_frame.pack(fill='both', expand=True)

# Memory Frame
memory_frame = tk.Frame(window)

buttons = [
    tk.Button(memory_frame, text='MC', bd=0),
    tk.Button(memory_frame, text='MR', bd=0),
    tk.Button(memory_frame, text='M+', bd=0),
    tk.Button(memory_frame, text='M-', bd=0),
    tk.Button(memory_frame, text='MS', bd=0),
    tk.Button(memory_frame, text='M▼', bd=0)
]

# Pack and bind events for each button
for btn in buttons:
    btn.pack(side='left', expand=True, fill='both')
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

memory_frame.pack(fill='x')

# Digits Frame
digits_frame = tk.Frame(window)

for col in range(4):  # configure columns 0 to 3
    digits_frame.columnconfigure(col, weight=1)

for row in range(6):  # row 0 to 5
    digits_frame.rowconfigure(row, weight=1)

# Buttons
# Row 0
perc_btn = tk.Button(digits_frame, text='%')
perc_btn.grid(row=0, column=0, sticky='news')

ce_btn = tk.Button(digits_frame, text='CE')
ce_btn.grid(row=0, column=1, sticky='news')

c_btn = tk.Button(digits_frame, text='C', command=clear_values)
c_btn.grid(row=0, column=2, sticky='news')

bkspace_btn = tk.Button(digits_frame, text='←')
bkspace_btn.grid(row=0, column=3, sticky='news')

# Row 1
fraction_btn = tk.Button(digits_frame, text='1/x')
fraction_btn.grid(row=1, column=0, sticky='news')

square_btn = tk.Button(digits_frame, text='x2')
square_btn.grid(row=1, column=1, sticky='news')

sq_root_btn = tk.Button(digits_frame, text='2/x')
sq_root_btn.grid(row=1, column=2, sticky='news')

divide_btn = tk.Button(digits_frame, text='/', command=lambda: operators(divide_btn))
divide_btn.grid(row=1, column=3, sticky='news')

# Row 2
btn_7 = tk.Button(digits_frame, text='7', command=lambda: display_values("7"))
btn_7.grid(row=2, column=0, sticky='news')

btn_8 = tk.Button(digits_frame, text='8', command=lambda: display_values("8"))
btn_8.grid(row=2, column=1, sticky='news')

btn_9 = tk.Button(digits_frame, text='9', command=lambda: display_values("9"))
btn_9.grid(row=2, column=2, sticky='news')

multiply_btn = tk.Button(digits_frame, text='*', command=lambda: operators(multiply_btn))
multiply_btn.grid(row=2, column=3, sticky='news')

# Row 3
btn_4 = tk.Button(digits_frame, text='4', command=lambda: display_values("4"))
btn_4.grid(row=3, column=0, sticky='news')

btn_5 = tk.Button(digits_frame, text='5', command=lambda: display_values("5"))
btn_5.grid(row=3, column=1, sticky='news')

btn_6 = tk.Button(digits_frame, text='6', command=lambda: display_values("6"))
btn_6.grid(row=3, column=2, sticky='news')

minus_btn = tk.Button(digits_frame, text='-', command=lambda: operators(minus_btn))
minus_btn.grid(row=3, column=3, sticky='news')

# Row 4
btn_1 = tk.Button(digits_frame, text='1', command=lambda: display_values("1"))
btn_1.grid(row=4, column=0, sticky='news')

btn_2 = tk.Button(digits_frame, text='2', command=lambda: display_values("2"))
btn_2.grid(row=4, column=1, sticky='news')

btn_3 = tk.Button(digits_frame, text='3', command=lambda: display_values("3"))
btn_3.grid(row=4, column=2, sticky='news')

add_btn = tk.Button(digits_frame, text='+', command=lambda: operators(add_btn))
add_btn.grid(row=4, column=3, sticky='news')

# Row 5
plus_minus_btn = tk.Button(digits_frame, text='+/-')
plus_minus_btn.grid(row=5, column=0, sticky='news')

btn_0 = tk.Button(digits_frame, text='0', command=lambda: display_values("0"))
btn_0.grid(row=5, column=1, sticky='news')

btn_dot = tk.Button(digits_frame, text='.')
btn_dot.grid(row=5, column=2, sticky='news')

equal_btn = tk.Button(digits_frame, text='=', bg='#2596be', fg='white', command=calculate)
equal_btn.grid(row=5, column=3, sticky='news')

for children in digits_frame.winfo_children():
    children.grid_configure(padx=1, pady=1)
    children['font'] = "Calibri 15"

digits_frame.pack(fill='both', expand=True)

window.mainloop()
