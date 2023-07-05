""" Instructions for building the Fibonacci sequence calculator. """

import tkinter as tk
from tkinter import font

def fibonacci_series():
    number = int(entry.get())
    a = 0
    b = 1
    fib_series = []
    while a < number:
        fib_series.append(a)
        a, b = b, a + b
    result_text.set(f'\nFibonacci Series: {fib_series}\n')


# Create the main window
window = tk.Tk()
window.title('Fibonacci Series Calculator')

# Set the desired font style, size, and family
font_style   = font.Font(family = 'Bahnschrift Light SemiCondensed',
                         size = 12, weight = 'bold')
font_style_2 = font.Font(family = 'Bahnschrift Light SemiCondensed',
                         size = 14, weight = 'bold')

# Create input label
input_label = tk.Label(window, 
                       text = '\nEnter the Number:\n', 
                       font = font_style)
input_label.pack()
entry = tk.Entry(window, font = font_style)
entry.pack()

# Create calculate button
calculate_button = tk.Button(window, 
                             text = 'Calculate', 
                             command = fibonacci_series, 
                             font = font_style)
calculate_button.pack()

# Create result label
result_text = tk.StringVar()
result_label = tk.Label(window, 
                        textvariable = result_text, 
                        justify = 'center', 
                        font = font_style_2)
result_label.pack()

# Start the main loop
window.mainloop()


# Ali_Khalaji
