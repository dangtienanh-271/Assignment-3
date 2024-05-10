import tkinter as tk
from tkinter import filedialog
from main import detect_objects

# File browser
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_objects(file_path)

# UI
root = tk.Tk()
root.title("Object Detection")
root.geometry("500x150")

btn_select_image = tk.Button(root, text="Select Image", command=select_image)
btn_select_image.pack(pady=20)

root.mainloop()
