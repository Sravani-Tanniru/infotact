
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import string
import pyperclip
from PIL import Image, ImageTk
import json

# File to store user credentials
CREDENTIALS_FILE = "users.json"
PASSWORDS_FILE = "saved_passwords.txt"
TEXT_FILE = "saved_text.txt"

# Load or initialize user credentials
def load_credentials():
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file)

def register():
    credentials = load_credentials()
    new_user = reg_username_entry.get()
    new_pass = reg_password_entry.get()
    
    if new_user in credentials:
        messagebox.showerror("Error", "Username already exists!")
    else:
        credentials[new_user] = new_pass
        save_credentials(credentials)
        messagebox.showinfo("Success", "Registration successful!")
        register_window.destroy()
        open_login()

def login():
    credentials = load_credentials()
    if username_entry.get() in credentials and credentials[username_entry.get()] == password_entry.get():
        login_window.destroy()
        open_main_app()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

def generate_password():
    length = int(password_length.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    pyperclip.copy(password)
    with open(PASSWORDS_FILE, "a") as file:
        file.write(password + "\n")
    messagebox.showinfo("Success", "Password copied to clipboard and saved!")

def save_text():
    content = text_editor.get("1.0", tk.END).strip()
    if content:
        with open(TEXT_FILE, "a") as file:
            file.write(content + "\n\n")
        messagebox.showinfo("Success", "Text appended successfully!")

def set_background(window, image_path):
    try:
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        label = tk.Label(window, image=bg_photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.lower()
        window.bg_photo = bg_photo
    except FileNotFoundError:
        messagebox.showwarning("Warning", f"Background image {image_path} not found! Running without background.")

def open_main_app():
    global text_editor, password_length, password_var
    root = tk.Tk()
    root.title("Password Manager & Text Editor")
    root.geometry("1200x800")
    set_background(root, "pass.webp")
    
    ttk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), background="white").pack(pady=20)
    password_length = ttk.Entry(root, width=15, font=("Arial", 14))
    password_length.insert(0, "12")
    password_length.pack(pady=10)
    
    password_var = tk.StringVar()
    password_entry = ttk.Entry(root, textvariable=password_var, width=40, state='readonly', font=("Arial", 14))
    password_entry.pack(pady=10)
    
    password_button = ttk.Button(root, text="Generate Password", command=generate_password)
    password_button.pack(pady=10)
    
    copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
    copy_button.pack(pady=10)
    
    ttk.Label(root, text="Text Editor", font=("Arial", 20, "bold"), background="white").pack(pady=20)
    text_editor = scrolledtext.ScrolledText(root, width=80, height=15, wrap=tk.WORD, font=("Arial", 14))
    text_editor.pack(padx=10, pady=10)
    
    save_button = ttk.Button(root, text="Save Text", command=save_text)
    save_button.pack(pady=10)
    
    root.mainloop()

def open_register():
    global register_window, reg_username_entry, reg_password_entry
    welcome_window.destroy()
    register_window = tk.Tk()
    register_window.title("Register")
    register_window.geometry("600x500")
    set_background(register_window, "regis.jpeg")
    
    ttk.Label(register_window, text="New Username: ", font=("Arial", 24), background="white").pack()
    reg_username_entry = ttk.Entry(register_window, font=("Arial", 24))
    reg_username_entry.pack(pady=20)
    
    ttk.Label(register_window, text="New Password: ", font=("Arial", 24), background="white").pack()
    reg_password_entry = ttk.Entry(register_window, show="*", font=("Arial", 24))
    reg_password_entry.pack(pady=20)
    
    register_button = ttk.Button(register_window, text="Register", command=register)
    register_button.pack(pady=20)

def open_login():
    global login_window, username_entry, password_entry
    welcome_window.destroy()
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("600x500")
    set_background(login_window, "log.jpg")
    
    ttk.Label(login_window, text="Username: ", font=("Arial", 24), background="white").pack()
    username_entry = ttk.Entry(login_window, font=("Arial", 24))
    username_entry.pack(pady=20)
    
    ttk.Label(login_window, text="Password: ", font=("Arial", 24), background="white").pack()
    password_entry = ttk.Entry(login_window, show="*", font=("Arial", 24))
    password_entry.pack(pady=20)
    
    login_button = ttk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=20)

# Welcome Window
welcome_window = tk.Tk()
welcome_window.title("Welcome")
welcome_window.geometry("600x500")
set_background(welcome_window, "welcome.png")

ttk.Label(welcome_window, text="Welcome to Password Manager", font=("Arial", 24, "bold")).pack(pady=20)
register_button = ttk.Button(welcome_window, text="Register", command=open_register)
register_button.pack(pady=20)

login_button = ttk.Button(welcome_window, text="Login", command=open_login)
login_button.pack(pady=20)

welcome_window.mainloop()
