import tkinter as tk
from tkinter import filedialog
import os

def select_path():
    path = filedialog.askdirectory(parent=root,
                                  initialdir="~/",
                                  title='Please select your workspace directory.')
    path_entry.delete(0, tk.END)
    path_entry.insert(0, path)

def save_path():
    path = path_entry.get()
    if not os.path.exists(os.path.join(path, 'build')):
        error_label.config(text="Error: No valid workspace found. If this is your first time building in this workspace, please run 'colcon build' manually.")
    else:
        with open(os.path.expanduser('~/.ros/coco_path.txt'), 'w') as file:
            file.write(path)
        root.destroy()

root = tk.Tk()
root.title("COCO Setup")

path_label = tk.Label(root, text="Set Workspace Path:")
path_entry = tk.Entry(root)
select_button = tk.Button(root, text="Select Path", command=select_path)
save_button = tk.Button(root, text="Save", command=save_path)
error_label = tk.Label(root, text="", fg="red")  # To display error messages

path_label.pack()
path_entry.pack()
select_button.pack()
save_button.pack()
error_label.pack()

root.mainloop()

