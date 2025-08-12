import tkinter as tk
from tkinter import ttk

def convert():
    try:
        temp = float(entry.get())
        unit = combo.get()
        if unit == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
        elif unit == "Celsius to Kelvin":
            result = temp + 273.15
        elif unit == "Kelvin to Celsius":
            result = temp - 273.15
        else:
            result = "Invalid"

        result_label.config(text=f"Result: {result:.2f}")
    except:
        result_label.config(text="Enter a valid number!")

root = tk.Tk()
root.title("Temperature Converter")

entry = tk.Entry(root)
entry.pack()

combo = ttk.Combobox(root, values=[
    "Celsius to Fahrenheit", "Fahrenheit to Celsius", 
    "Celsius to Kelvin", "Kelvin to Celsius"
])
combo.pack()
combo.set("Celsius to Fahrenheit")

tk.Button(root, text="Convert", command=convert).pack()
result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
