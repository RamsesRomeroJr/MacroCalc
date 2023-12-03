import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

class Calculator:
    def __init__(self):
        self.total_macros = [0, 0, 0, 0]
        self.food_nutrients_dict = {}

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

        self.askAdvice_button = ttk.Button(self.window, text="Advice? Ask", command=self.ask_AI)
        self.askAdvice_button.grid(row=9, column=0, padx=10, pady=5)
        self.ask_entry = tk.Text(self.window, height=10, width=30)
        self.ask_entry.grid(row=9, column=1, padx=10, pady=5)

        self.window.geometry("450x450")
        self.window.title("Calorie Calculator")
        self.window.mainloop()


    def on_add_food(self):

        food_name = self.food_entry.get()
        calories_value = self.calories_entry.get()
        protein_value = self.protein_entry.get()
        carbs_value = self.carbs_entry.get()
        fats_value = self.fats_entry.get()
        self.total_macros[0] += int(calories_value)
        self.total_macros[1] += int(protein_value)
        self.total_macros[2] += int(carbs_value)
        self.total_macros[3] += int(fats_value)

        self.food_nutrients_dict[food_name] = [calories_value, protein_value, carbs_value, fats_value]

        self.food_entry.delete(0, 'end')
        self.calories_entry.delete(0, 'end')
        self.protein_entry.delete(0, 'end')
        self.carbs_entry.delete(0, 'end')
        self.fats_entry.delete(0, 'end')

        calculate_button = ttk.Button(self.window, text="Calculate", command=self.calculate)
        calculate_button.grid(row=7, column=0, padx=10, pady=5)

        recipe_button = ttk.Button(self.window, text="Create Recipe", command=self.give_me_recipe)
        recipe_button.grid(row=8, column=0, padx=10, pady=5)

    def calculate(self):
        results = tk.Tk()
        results.title("results")

        total_macros_header = ttk.Label(results, text="Total macros:")
        total_macros_header.grid(row=0, column=0, padx=5, pady=5)

        calories_info = ttk.Label(results, text=f'Calories = {self.total_macros[0]}')
        calories_info.grid(row=1, column=0, padx=10, pady=5)

        protein_info = ttk.Label(results, text=f'protein = {self.total_macros[1]}')
        protein_info.grid(row=2, column=0, padx=10, pady=5)

        carbs_info = ttk.Label(results, text=f'carbs = {self.total_macros[2]}')
        carbs_info.grid(row=3, column=0, padx=7, pady=5)

        fats_info = ttk.Label(results, text=f'fats = {self.total_macros[3]}')
        fats_info.grid(row=4, column=0, padx=5, pady=5)

        header = ttk.Label(results, text="Food and Nutrients:")
        header.grid(row=5, column=0, padx=5, pady=5)

        count = 0

        for food, macros in self.food_nutrients_dict.items():

            food_header = ttk.Label(results, text=f'{food}')
            food_header.grid(row=6, column=0 + count, padx=5, pady=5)

            calorie_header = ttk.Label(results, text=f'calories = {macros[0]}')
            calorie_header.grid(row=7, column=0 + count, padx=5, pady=5)

            protein_header = ttk.Label(results, text=f'protein = {macros[1]}')
            protein_header.grid(row=8, column=0 + count, padx=5, pady=5)

            carb_header = ttk.Label(results, text=f'carbs = {macros[2]}')
            carb_header.grid(row=9, column=0 + count, padx=5, pady=5)

            fats_header = ttk.Label(results, text=f'fats = {macros[3]}')
            fats_header.grid(row=10, column=0 + count, padx=5, pady=5)

            count += 1
    def ask_AI(self):
        aiResponseWindow = tk.Tk()
        aiResponseWindow.title("Ai SAID")
        aiResponseWindow.geometry("500x500")

        ask_value = self.ask_entry.get('1.0', tk.END)
        url = "https://open-ai25.p.rapidapi.com/ask"

        payload = { "query": f'{ask_value}' }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "open-ai25.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        aiResponse = tk.Label(aiResponseWindow, text=f'{response.json()["response"]}', wraplength=350, justify="left")
        aiResponse.grid(row=0, column=0, padx=5, pady=5)

    def give_me_recipe(self):
        receipeWindow = tk.Tk()
        receipeWindow.title("New Recipe")
        receipeWindow.geometry("500x500")

        foodsArray = []
        for food in self.food_nutrients_dict.items():
            foodsArray.append(food)

        url = "https://open-ai25.p.rapidapi.com/ask"

        payload = { "query": f'Give me a recipe with the following items: {foodsArray}' }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "open-ai25.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        aiResponse = tk.Label(receipeWindow, text=f'{response.json()["response"]}', wraplength=350, justify="left")
        aiResponse.grid(row=0, column=0, padx=5, pady=5)

Calculator()
