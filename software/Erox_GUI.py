import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import time
import pywinauto
from pywinauto.keyboard import send_keys
from pywinauto.application import Application
from queue import Queue
import threading


# Global queue to store file paths
file_queue = Queue()

# Global variable to control printing loop
printing_flag = threading.Event()
printing_flag.set()  # Set to True initially

def start_printing(file_path):
    progmam_path = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"
    try:
        app = Application().start(r'{} "{}"'.format(progmam_path, file_path))
        time.sleep(3)
        send_keys('^a^P')
        time.sleep(4)

        w_handle = pywinauto.findwindows.find_windows(title=u'Print')[0]
        window = app.window(handle=w_handle)
        window.wait('ready', timeout=10)

        if not printing_flag.is_set():
            window.Cancel.click()  # Stop printing
            return

        window[u'Print in gra&yscale(black and white)'].click()
        time.sleep(2)

        window[u'Shrink oversized pages'].click()
        time.sleep(2)

        window[u'Auto'].click()
        time.sleep(2)

        window.Print.click()
        window.wait_not('visible')  # Wait until the printing is completed
        file_queue.get()  # Remove the file path from the queue

        if not file_queue.empty():
            next_file_path = file_queue.queue[0]
            start_printing(next_file_path)
    except(Exception):
        print(Exception)

def select_file():
    file_path = askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_name = os.path.basename(file_path)
        queue_table.insert('', 'end', values=(len(queue_table.get_children()) + 1, file_name, 'ID123', 'TypeX', 'ColorY', 'PaymentZ', 'Pending'))
        file_queue.put(file_path)

def start_printing_from_queue():
    if file_queue.empty():
        print("No files in the queue.")
    else:
        printing_flag.set()  # Set the printing flag to True
        file_path = file_queue.queue[0]
        start_printing(file_path)

def stop_printing():
    printing_flag.clear()  # Set the printing flag to False
    print("Printing stopped.")
root = tk.Tk()
root.title("erox")
root.geometry("700x600")
root.configure(bg="white")  # Background color

title_label = tk.Label(root, text="Welcome To erox", font=("Arial", 45), bg="white")  # White background
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

menu_container = tk.Frame(root, width=50, bg='lightgray')
menu_container.place(relx=0, rely=0.2, relheight=0.8)

########################################################################################
menu_buttons = [
    "Profile",
    "Report Problem",
    "About Us",
    "Logout"
]

for i, btn_text in enumerate(menu_buttons):
    btn = tk.Button(menu_container, text=btn_text, bg='lightblue', fg='black', font=("Arial", 12))
    btn.grid(row=i, column=0, padx=10, pady=5, sticky='ew')  # Added sticky to expand button width

########################################################################################
columns = ("Sr No.", "File Name", "ID", "Type", "Color", "Payment", "Status")
queue_table = ttk.Treeview(root, columns=columns, show='headings', height=15)
queue_table.place(relx=0.1, rely=0.2, relwidth=0.7, relheight=0.8)

for col in columns:
    queue_table.heading(col, text=col)
    queue_table.column(col, width=200)

########################################################################################
select_file_btn = tk.Button(root, text="Select File", command=select_file, bg='lightgreen', fg='black', font=("Arial", 12))
select_file_btn.place(relx=0.8, rely=0.3, anchor=tk.CENTER)

start_printing_btn = tk.Button(root, text="Start Printing", command=start_printing_from_queue, bg='lightgreen', fg='black', font=("Arial", 12))
start_printing_btn.place(relx=0.8, rely=0.4, anchor=tk.CENTER)

stop_printing_btn = tk.Button(root, text="Stop Printing", command=stop_printing, bg='lightcoral', fg='black', font=("Arial", 12))
stop_printing_btn.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

########################################################################################

root.mainloop()
