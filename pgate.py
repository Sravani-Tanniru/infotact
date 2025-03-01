# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox
# import random
# import string
# import pyperclip

# def generate_password():
#     length = int(password_length.get())
#     chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(chars) for _ in range(length))
#     password_var.set(password)

# def copy_to_clipboard():
#     pyperclip.copy(password_var.get())
#     messagebox.showinfo("Success", "Password copied to clipboard!")

# def save_text():
#     content = text_editor.get("1.0", tk.END)
#     with open("saved_text.txt", "w") as file:
#         file.write(content)
#     messagebox.showinfo("Success", "Text saved successfully!")

# # Main window
# root = tk.Tk()
# root.title("Password Generator & Text Editor")
# root.geometry("500x500")

# # Password Generator Frame
# password_frame = ttk.LabelFrame(root, text="Password Generator")
# password_frame.pack(padx=10, pady=10, fill="both", expand=True)

# password_length = ttk.Entry(password_frame, width=10)
# password_length.insert(0, "12")
# password_length.pack(pady=5)

# password_var = tk.StringVar()
# password_entry = ttk.Entry(password_frame, textvariable=password_var, width=30, state='readonly')
# password_entry.pack(pady=5)

# password_button = ttk.Button(password_frame, text="Generate Password", command=generate_password)
# password_button.pack(pady=5)

# copy_button = ttk.Button(password_frame, text="Copy to Clipboard", command=copy_to_clipboard)
# copy_button.pack(pady=5)

# # Text Editor Frame
# text_frame = ttk.LabelFrame(root, text="Text Editor")
# text_frame.pack(padx=10, pady=10, fill="both", expand=True)

# text_editor = scrolledtext.ScrolledText(text_frame, width=50, height=10, wrap=tk.WORD)
# text_editor.pack(padx=5, pady=5)

# save_button = ttk.Button(text_frame, text="Save Text", command=save_text)
# save_button.pack(pady=5)

# # Run the GUI
# root.mainloop()
# -----------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox
# import random
# import string
# import pyperclip

# # List to store copied passwords
# copied_passwords = []

# def generate_password():
#     length = int(password_length.get())
#     chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(chars) for _ in range(length))
#     password_var.set(password)

# def copy_to_clipboard():
#     copied_password = password_var.get()
#     if copied_password:
#         pyperclip.copy(copied_password)
#         copied_passwords.append(copied_password)  # Store copied password
#         messagebox.showinfo("Success", "Password copied to clipboard!")

# def save_text():
#     content = text_editor.get("1.0", tk.END).strip()
#     with open("saved_text.txt", "w") as file:
#         file.write(content)
#     messagebox.showinfo("Success", "Text saved successfully!")

# # Function to view copied passwords in a new window
# def view_copied_passwords():
#     if not copied_passwords:
#         messagebox.showinfo("No Passwords", "No passwords copied yet.")
#         return

#     view_window = tk.Toplevel(root)
#     view_window.title("Copied Passwords")
#     view_window.geometry("300x200")

#     tk.Label(view_window, text="Copied Passwords:", font=("Arial", 12, "bold")).pack(pady=5)

#     text_area = tk.Text(view_window, height=8, width=30)
#     text_area.pack()
#     text_area.insert(tk.END, "\n".join(copied_passwords))
#     text_area.config(state="disabled")

# # Main window
# root = tk.Tk()
# root.title("Password Generator & Text Editor")
# root.geometry("500x500")

# # Password Generator Frame
# password_frame = ttk.LabelFrame(root, text="Password Generator")
# password_frame.pack(padx=10, pady=10, fill="both", expand=True)

# password_length = ttk.Entry(password_frame, width=10)
# password_length.insert(0, "12")
# password_length.pack(pady=5)

# password_var = tk.StringVar()
# password_entry = ttk.Entry(password_frame, textvariable=password_var, width=30, state='readonly')
# password_entry.pack(pady=5)

# password_button = ttk.Button(password_frame, text="Generate Password", command=generate_password)
# password_button.pack(pady=5)

# copy_button = ttk.Button(password_frame, text="Copy to Clipboard", command=copy_to_clipboard)
# copy_button.pack(pady=5)

# # **New Button to View Copied Passwords**
# view_button = ttk.Button(password_frame, text="View Copied Passwords", command=view_copied_passwords)
# view_button.pack(pady=5)

# # Text Editor Frame
# text_frame = ttk.LabelFrame(root, text="Text Editor")
# text_frame.pack(padx=10, pady=10, fill="both", expand=True)

# text_editor = scrolledtext.ScrolledText(text_frame, width=50, height=10, wrap=tk.WORD)
# text_editor.pack(padx=5, pady=5)

# save_button = ttk.Button(text_frame, text="Save Text", command=save_text)
# save_button.pack(pady=5)

# # Run the GUI
# root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox, filedialog
# import random
# import string
# import pyperclip

# # List to store copied passwords
# copied_passwords = []

# def generate_password():
#     """Generate a random password and display it in the entry field."""
#     try:
#         length = int(password_length.get())
#         if length <= 0:
#             raise ValueError
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid positive number for password length.")
#         return

#     chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(chars) for _ in range(length))
#     password_var.set(password)

# def copy_to_clipboard():
#     """Copy generated password to clipboard and store it."""
#     password = password_var.get()
#     if password:
#         pyperclip.copy(password)
#         copied_passwords.append(password)  # Store copied password
#         messagebox.showinfo("Success", "Password copied to clipboard!")

# def save_text():
#     """Save text from the editor to a user-specified file."""
#     content = text_editor.get("1.0", tk.END).strip()
    
#     if not content:
#         messagebox.showwarning("Warning", "Text editor is empty. Nothing to save!")
#         return

#     file_path = filedialog.asksaveasfilename(
#         defaultextension=".txt",
#         filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
#     )

#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(content)
#         messagebox.showinfo("Success", f"Text saved successfully at:\n{file_path}")

# def view_copied_passwords():
#     """Display a separate window showing all copied passwords."""
#     if not copied_passwords:
#         messagebox.showinfo("Info", "No passwords copied yet.")
#         return

#     # Create a new window
#     view_window = tk.Toplevel(root)
#     view_window.title("Copied Passwords")
#     view_window.geometry("400x300")

#     label = tk.Label(view_window, text="Copied Passwords", font=("Arial", 12, "bold"))
#     label.pack(pady=5)

#     text_box = scrolledtext.ScrolledText(view_window, width=40, height=10, wrap=tk.WORD)
#     text_box.pack(padx=5, pady=5)
#     text_box.insert(tk.END, "\n".join(copied_passwords))
#     text_box.config(state=tk.DISABLED)

# # Main window
# root = tk.Tk()
# root.title("Password Generator & Text Editor")
# root.geometry("500x550")

# # Password Generator Frame
# password_frame = ttk.LabelFrame(root, text="Password Generator")
# password_frame.pack(padx=10, pady=10, fill="both", expand=True)

# password_length = ttk.Entry(password_frame, width=10)
# password_length.insert(0, "12")
# password_length.pack(pady=5)

# password_var = tk.StringVar()
# password_entry = ttk.Entry(password_frame, textvariable=password_var, width=30, state='readonly')
# password_entry.pack(pady=5)

# password_button = ttk.Button(password_frame, text="Generate Password", command=generate_password)
# password_button.pack(pady=5)

# copy_button = ttk.Button(password_frame, text="Copy to Clipboard", command=copy_to_clipboard)
# copy_button.pack(pady=5)

# view_button = ttk.Button(password_frame, text="View Copied Passwords", command=view_copied_passwords)
# view_button.pack(pady=5)

# # Text Editor Frame
# text_frame = ttk.LabelFrame(root, text="Text Editor")
# text_frame.pack(padx=10, pady=10, fill="both", expand=True)

# text_editor = scrolledtext.ScrolledText(text_frame, width=50, height=10, wrap=tk.WORD)
# text_editor.pack(padx=5, pady=5)

# save_button = ttk.Button(text_frame, text="Save Text", command=save_text)
# save_button.pack(pady=5)

# # Run the GUI
# root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------
# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox, filedialog
# from PIL import Image, ImageTk
# import random
# import string
# import pyperclip
# import os

# # File paths for saving data
# PASSWORDS_FILE = "saved_passwords.txt"
# TEXT_FILE = "saved_texts.txt"

# # Load previously saved passwords
# def load_passwords():
#     if os.path.exists(PASSWORDS_FILE):
#         with open(PASSWORDS_FILE, "r") as file:
#             return file.read().strip().split("\n")
#     return []

# # Load previously saved texts
# def load_text():
#     if os.path.exists(TEXT_FILE):
#         with open(TEXT_FILE, "r") as file:
#             return file.read()
#     return ""

# # Store copied passwords
# copied_passwords = load_passwords()

# # Function to generate a password
# def generate_password():
#     try:
#         length = int(password_length.get())
#         if length <= 0:
#             raise ValueError
#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid positive number for password length.")
#         return

#     chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(chars) for _ in range(length))
#     password_var.set(password)

# # Function to copy the password
# def copy_to_clipboard():
#     password = password_var.get()
#     if password:
#         pyperclip.copy(password)
#         copied_passwords.append(password)

#         # Save copied passwords to a file
#         with open(PASSWORDS_FILE, "a") as file:
#             file.write(password + "\n")

#         messagebox.showinfo("Success", "Password copied to clipboard!")

# # Function to save text
# def save_text():
#     content = text_editor.get("1.0", tk.END).strip()
    
#     if not content:
#         messagebox.showwarning("Warning", "Text editor is empty. Nothing to save!")
#         return

#     with open(TEXT_FILE, "w") as file:
#         file.write(content)

#     messagebox.showinfo("Success", "Text saved successfully!")

# # Function to view copied passwords
# def view_copied_passwords():
#     if not copied_passwords:
#         messagebox.showinfo("Info", "No passwords copied yet.")
#         return

#     view_window = tk.Toplevel(root)
#     view_window.title("Copied Passwords")
#     view_window.geometry("400x300")

#     label = tk.Label(view_window, text="Copied Passwords", font=("Arial", 12, "bold"))
#     label.pack(pady=5)

#     text_box = scrolledtext.ScrolledText(view_window, width=40, height=10, wrap=tk.WORD)
#     text_box.pack(padx=5, pady=5)
#     text_box.insert(tk.END, "\n".join(copied_passwords))
#     text_box.config(state=tk.DISABLED)

# # Function to view saved text
# def view_saved_text():
#     saved_text = load_text()
#     if not saved_text:
#         messagebox.showinfo("Info", "No saved text available.")
#         return

#     text_window = tk.Toplevel(root)
#     text_window.title("Saved Text")
#     text_window.geometry("400x300")

#     label = tk.Label(text_window, text="Saved Text", font=("Arial", 12, "bold"))
#     label.pack(pady=5)

#     text_box = scrolledtext.ScrolledText(text_window, width=40, height=10, wrap=tk.WORD)
#     text_box.pack(padx=5, pady=5)
#     text_box.insert(tk.END, saved_text)
#     text_box.config(state=tk.DISABLED)

# # Main window
# root = tk.Tk()
# root.title("Password Generator & Text Editor")
# root.geometry("600x600")

# # Load background image for main window
# bg_image = Image.open("pass.webp")  # Replace with your image file
# bg_image = bg_image.resize((600, 600), Image.LANCZOS)
# bg_photo = ImageTk.PhotoImage(bg_image)

# canvas = tk.Canvas(root, width=600, height=600)
# canvas.pack(fill="both", expand=True)
# canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# # Password Generator Frame
# password_frame = ttk.LabelFrame(root, text="Password Generator")
# password_frame.place(x=100, y=50, width=400, height=230)

# password_length = ttk.Entry(password_frame, width=10)
# password_length.insert(0, "12")
# password_length.pack(pady=5)

# password_var = tk.StringVar()
# password_entry = ttk.Entry(password_frame, textvariable=password_var, width=30, state='readonly')
# password_entry.pack(pady=5)

# password_button = ttk.Button(password_frame, text="Generate Password", command=generate_password)
# password_button.pack(pady=5)

# copy_button = ttk.Button(password_frame, text="Copy to Clipboard", command=copy_to_clipboard)
# copy_button.pack(pady=5)

# view_button = ttk.Button(password_frame, text="View Copied Passwords", command=view_copied_passwords)
# view_button.pack(pady=5)

# # Text Editor Frame
# text_frame = ttk.LabelFrame(root, text="Text Editor")
# text_frame.place(x=100, y=320, width=400, height=200)

# text_editor = scrolledtext.ScrolledText(text_frame, width=40, height=7, wrap=tk.WORD)
# text_editor.pack(padx=5, pady=5)
# text_editor.insert(tk.END, load_text())  # Load saved text into the editor

# save_button = ttk.Button(text_frame, text="Save Text", command=save_text)
# save_button.pack(pady=5)

# view_text_button = ttk.Button(text_frame, text="View Saved Text", command=view_saved_text)
# view_text_button.pack(pady=5)

# # Run the GUI
# root.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------
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
