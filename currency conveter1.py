# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:04:27 2025

@author: Lali
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import json
import os
import matplotlib.pyplot as plt

# Global user data file
USER_DATA_FILE = "users.json"

# Helper function to load user data
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as file:
        return json.load(file)

# Helper function to save user data
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file)

# Helper function to set background image
def set_background(window, image_path):
    image = Image.open(image_path)
    image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
    background_image = ImageTk.PhotoImage(image)

    background_label = tk.Label(window, image=background_image)
    background_label.image = background_image  # Keep a reference to prevent garbage collection
    background_label.place(relwidth=1, relheight=1)  # Cover the entire window

# Registration Page
def register_page(previous_window):
    previous_window.destroy()

    def register_user():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        user_data = load_user_data()

        if username in user_data:
            messagebox.showerror("Error", "Username already exists!")
            return

        user_data[username] = password
        save_user_data(user_data)
        messagebox.showinfo("Success", "Registration successful!")
        register_window.destroy()
        main_page()

    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("800x600")
    set_background(register_window, "C:\\Users\\srava\\OneDrive\\Desktop\\Coding files\\infotact projects\\bgimg.jpg")

    tk.Label(register_window, text="Register", font=("Arial", 24), bg="white").pack(pady=20)

    tk.Label(register_window, text="Username", font=("Arial", 16), bg="white").pack(pady=5)
    username_entry = tk.Entry(register_window, font=("Arial", 14), width=30)
    username_entry.pack(pady=5)

    tk.Label(register_window, text="Password", font=("Arial", 16), bg="white").pack(pady=5)
    password_entry = tk.Entry(register_window, show="*", font=("Arial", 14), width=30)
    password_entry.pack(pady=5)

    tk.Button(register_window, text="Register", font=("Arial", 16), width=15, command=register_user).pack(pady=20)

# Login Page
def login_page(previous_window):
    previous_window.destroy()

    def authenticate():
        username = username_entry.get()
        password = password_entry.get()

        user_data = load_user_data()

        if username in user_data and user_data[username] == password:
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
            currency_converter_page()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("800x600")
    set_background(login_window, "C:\\Users\\srava\\OneDrive\\Desktop\\Coding files\\infotact projects\\bgimg.jpg")

    tk.Label(login_window, text="Login", font=("Arial", 24), bg="white").pack(pady=20)

    tk.Label(login_window, text="Username", font=("Arial", 16), bg="white").pack(pady=5)
    username_entry = tk.Entry(login_window, font=("Arial", 14), width=30)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password", font=("Arial", 16), bg="white").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 14), width=30)
    password_entry.pack(pady=5)

    tk.Button(login_window, text="Login", font=("Arial", 16), width=15, command=authenticate).pack(pady=10)
    tk.Button(login_window, text="Register", font=("Arial", 16), width=15, command=lambda: register_page(login_window)).pack(pady=10)

# Currency Converter Page
def currency_converter_page():
    currency_options = [
        "USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY", "CHF",
        "NZD", "SEK", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "ZAR", "BRL"
    ]

    def convert_currency():
        amount = amount_entry.get()

        try:
            amount = float(amount)
            if amount < 0:
                messagebox.showerror("Error", "Amount cannot be negative.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number.")
            return

        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            messagebox.showerror("Error", "Select different currencies for conversion.")
            return

        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

        try:
            response = requests.get(api_url)
            data = response.json()

            if to_currency in data["rates"]:
                rate = data["rates"][to_currency]
                converted_amount = amount * rate
                result_label.config(
                    text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
                )
            else:
                messagebox.showerror("Error", "Currency not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def plot_graph(plot_type):
        from_currency = from_currency_var.get()
        target_currencies = ["USD", "EUR", "GBP", "INR", "AUD", "JPY"]

        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

        try:
            response = requests.get(api_url)
            data = response.json()

            if "rates" in data:
                rates = {currency: data["rates"].get(currency, 0) for currency in target_currencies}
                currencies = list(rates.keys())
                values = list(rates.values())

                if plot_type == "line":
                    plt.plot(currencies, values, marker='o', color='blue')
                elif plot_type == "bar":
                    plt.bar(currencies, values, color='skyblue')
                elif plot_type == "pie":
                    plt.pie(values, labels=currencies, autopct='%1.1f%%')

                plt.title(f"Exchange Rates Against {from_currency}")
                plt.show()
            else:
                messagebox.showerror("Error", "Failed to fetch exchange rates.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    converter_window = tk.Tk()
    converter_window.title("Currency Converter")
    converter_window.geometry("800x600")
    set_background(converter_window, "C:\\Users\\srava\\OneDrive\\Desktop\\Coding files\\infotact projects\\1.webp")

    tk.Label(converter_window, text="Currency Converter", font=("Arial", 24), bg="white").pack(pady=20)

    tk.Label(converter_window, text="Amount", font=("Arial", 16), bg="white").pack(pady=5)
    amount_entry = tk.Entry(converter_window, font=("Arial", 14), width=30)
    amount_entry.pack(pady=5)

    tk.Label(converter_window, text="From Currency", font=("Arial", 16), bg="white").pack(pady=5)
    from_currency_var = tk.StringVar(converter_window)
    from_currency_var.set(currency_options[0])
    from_currency_menu = tk.OptionMenu(converter_window, from_currency_var, *currency_options)
    from_currency_menu.config(font=("Arial", 14))
    from_currency_menu.pack(pady=5)

    tk.Label(converter_window, text="To Currency", font=("Arial", 16), bg="white").pack(pady=5)
    to_currency_var = tk.StringVar(converter_window)
    to_currency_var.set(currency_options[1])
    to_currency_menu = tk.OptionMenu(converter_window, to_currency_var, *currency_options)
    to_currency_menu.config(font=("Arial", 14))
    to_currency_menu.pack(pady=5)

    tk.Button(converter_window, text="Convert", font=("Arial", 16), width=15, command=convert_currency).pack(pady=10)

    result_label = tk.Label(converter_window, text="", font=("Arial", 14), bg="white")
    result_label.pack(pady=20)

    tk.Button(converter_window, text="Plot Line Chart", font=("Arial", 16), width=20, command=lambda: plot_graph("line")).pack(pady=5)
    tk.Button(converter_window, text="Plot Bar Chart", font=("Arial", 16), width=20, command=lambda: plot_graph("bar")).pack(pady=5)
    tk.Button(converter_window, text="Plot Pie Chart", font=("Arial", 16), width=20, command=lambda: plot_graph("pie")).pack(pady=5)

    converter_window.mainloop()

# Main Page
def main_page():
    window = tk.Tk()
    window.title("Main Page")
    window.geometry("800x600")
    set_background(window, "C:\\Users\\srava\\OneDrive\\Desktop\\Coding files\\infotact projects\\2.jpg")

    tk.Label(window, text="Welcome to Currency Converter", font=("Arial", 24), bg="white").pack(pady=20)

    tk.Button(window, text="Login", font=("Arial", 16), width=15, command=lambda: login_page(window)).pack(pady=10)
    tk.Button(window, text="Register", font=("Arial", 16), width=15, command=lambda: register_page(window)).pack(pady=10)

    window.mainloop()

# Run the app
main_page()
