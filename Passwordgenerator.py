import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_entry.get()
    
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return
    
    length = int(length)
    
    if length <= 0:
        messagebox.showerror("Error", "Please enter a positive number for length.")
        return
    
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    
    if not is_strong_password(password):
        messagebox.showwarning("Warning", "Generated password may not be strong. Consider increasing length.")
    
    password_display.config(state="normal")
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state="disabled")

def is_strong_password(password):
    # You can define your own criteria for a strong password here
    # For simplicity, we'll just check if the length is at least 8 characters
    return len(password) >= 8

def reset_password():
    length_entry.delete(0, tk.END)
    password_display.config(state="normal")
    password_display.delete(1.0, tk.END)
    password_display.config(state="disabled")

root = tk.Tk()
root.title("Password Generator")

# Colorful Background
background_color = "blue"  
root.configure(background=background_color)

username_label = tk.Label(root, text="Username:", bg=background_color)
