import tkinter as tk
from tkinter import filedialog

def choose_dir():
    dir_path_search = filedialog.askdirectory()
    if dir_path_search:
        label_search_dir.config(text=f"Ausgewählter Pfad: {dir_path_search}")
    # todo - add logic

def readTextfield():
    content = file_type_text.get("1.0", tk.END)
    # todo - add logic / remove print
    print(f"Textfeld-Inhalt:\n{content}")

def start_search():
    # todo - add logic / remove print
    print(f"Button 'Suchen' pressed!")

def choose_output():
    dir_path_output = filedialog.askdirectory()
    if dir_path_output:
        label_output_file.config(text=f"Ausgewählter Pfad: {dir_path_output}")
    
    # todo - add logic

root = tk.Tk()
root.title("Suche Dateitypen")

window_width = 380
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calc window position - middle of screen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.minsize(window_width, window_height)
root.maxsize(700, 500)

# ini frames
choose_dir_frame_top = tk.Frame(root, pady=5, padx=20)#, bg="lightblue") 
choose_dir_frame_top.grid(row=0, column=0, sticky="w")

choose_dir_frame = tk.Frame(root, pady=5, padx=20)#, bg="lightcoral")
choose_dir_frame.grid(row=1, column=0, sticky="w")

file_type_frame = tk.Frame(root, pady=10, padx=20)#, bg="lightgreen")
file_type_frame.grid(row=2, column=0, sticky="w")

output_file_frame =tk.Frame(root, pady=5, padx=20)#, bg="skyblue")
output_file_frame.grid(row=3, column=0, sticky="w")

# choose_dir_frame_top
label_search_dir_desc = tk.Label(choose_dir_frame_top, text="Verzeichnis zum durchsuchen auswählen")
label_search_dir_desc.grid(row=0, column=0, sticky="w")
choose_dir_frame_top.grid_columnconfigure(0)

# choose_dir_frame
label_search_dir = tk.Label(choose_dir_frame, text="Kein Verzeichnis ausgewählt")
label_search_dir.grid(row=0, column=0, sticky="w")

choose_dir_frame.grid_columnconfigure(1, minsize=10)

buttonChoose = tk.Button(choose_dir_frame, text="Verzeichnis auswählen", command=choose_dir)
buttonChoose.grid(row=0, column=2, sticky="e")

# file_type_frame
file_type_text = tk.Text(file_type_frame, height=1, width=20)
file_type_text.grid(row=0, column=0, sticky="w")

file_type_frame.grid_columnconfigure(1, minsize=10)

buttonSearch = tk.Button(file_type_frame, text="Suchen", command=start_search)
buttonSearch.grid(row=0, column=2)

# output_file_frame
label_output = tk.Label(output_file_frame, text="Ausgabe nach:")
label_output.grid(row=0, column=0, sticky="w")

label_output_file = tk.Label(output_file_frame, text="Kein Verzeichnis ausgewählt")
label_output_file.grid(row=1, column=0, sticky="w")

output_file_frame.grid_columnconfigure(1, minsize=10)

button_output_file = tk.Button(output_file_frame, text="Verzeichnis auswählen", command=choose_output)
button_output_file.grid(row=1, column=2)


root.mainloop()
