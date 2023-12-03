import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.total_macros = [0, 0, 0, 0]

        self.window = tk.Tk()
        self.food_label = ttk.Label(self.window, text="Food:")
        self.food_label.grid(row=0, column=0, padx=10, pady=5)
        self.food_entry = ttk.Entry(self.window)
        self.food_entry.grid(row=0, column=1, padx=10, pady=5)

        self.calories_label = ttk.Label(self.window, text="Calories:")
        self.calories_label.grid(row=1, column=0, padx=10, pady=5)
        self.calories_entry = ttk.Entry(self.window)
        self.calories_entry.grid(row=1, column=1, padx=10, pady=5)

        self.protein_label = ttk.Label(self.window, text="protein:")
        self.protein_label.grid(row=2, column=0, padx=10, pady=5)
        self.protein_entry = ttk.Entry(self.window)
        self.protein_entry.grid(row=2, column=1, padx=10, pady=5)

        self.carbs_label = ttk.Label(self.window, text="Carbs:")
        self.carbs_label.grid(row=3, column=0, padx=10, pady=5)
        self.carbs_entry = ttk.Entry(self.window)
        self.carbs_entry.grid(row=3, column=1, padx=10, pady=5)

        self.fats_label = ttk.Label(self.window, text="Fats:")
        self.fats_label.grid(row=4, column=0, padx=10, pady=5)
        self.fats_entry = ttk.Entry(self.window)
        self.fats_entry.grid(row=4, column=1, padx=10, pady=5)

        self.addFood_button = ttk.Button(self.window, text="Add Food", command=self.on_add_food)
        self.addFood_button.grid(row=6, column=0, padx=10, pady=5)
        self.window.geometry("350x350")
        self.window.title("Calorie Calculator")
        self.window.mainloop()


    def on_add_food(self):

        calories_value = self.calories_entry.get()
        protein_value = self.protein_entry.get()
        carbs_value = self.carbs_entry.get()
        fats_value = self.fats_entry.get()
        self.total_macros[0] += int(calories_value)
        self.total_macros[1] += int(protein_value)
        self.total_macros[2] += int(carbs_value)
        self.total_macros[3] += int(fats_value)

        self.food_entry.delete(0, 'end')
        self.calories_entry.delete(0, 'end')
        self.protein_entry.delete(0, 'end')
        self.carbs_entry.delete(0, 'end')
        self.fats_entry.delete(0, 'end')

        calculate_button = ttk.Button(self.window, text="Calculate", command=self.calculate)
        calculate_button.grid(row=5, column=0, padx=10, pady=5)

    def calculate(self):
        print("Here's your meal's macros")
        print("calories = " , self.total_macros[0])
        print("protein = " , self.total_macros[1])
        print("carbs = " , self.total_macros[2])
        print("fats = " , self.total_macros[3])







Calculator()
