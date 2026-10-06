from organizer import organize_files
import customtkinter as ctk
from tkinter import filedialog

selected_folder = ""

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Smart File Organizer")
app.geometry("900x600")


def select_folder():
    global selected_folder

    folder = filedialog.askdirectory()

    if folder:
        selected_folder = folder
        status.configure(text=f"Selected: {folder}")

def organize_selected_folder():

    if selected_folder:
        organize_files(selected_folder)
        status.configure(text="✓ Files organized successfully!")

    else:
        status.configure(text="Please select a folder first.")


title = ctk.CTkLabel(
    app,
    text="Smart File Organizer",
    font=("Arial", 32, "bold")
)
title.pack(pady=(50, 10))


subtitle = ctk.CTkLabel(
    app,
    text="Organize your files effortlessly",
    font=("Arial", 16)
)
subtitle.pack(pady=(0, 40))


folder_button = ctk.CTkButton(
    app,
    text="📂  Select Folder",
    width=250,
    height=50,
    font=("Arial", 16),
    command=select_folder
)
folder_button.pack(pady=20)


organize_button = ctk.CTkButton(
    app,
    text="✨  Organize Files",
    width=250,
    height=50,
    font=("Arial", 16),
    command=organize_selected_folder
)
organize_button.pack(pady=20)


status = ctk.CTkLabel(
    app,
    text="No folder selected",
    font=("Arial", 14)
)
status.pack(pady=30)


app.mainloop()
