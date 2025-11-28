import os
import sys
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox


def rename_files():
    file_path = filedialog.askdirectory(title="Select a folder with files")
    if not file_path:
        return

    if not os.path.exists(file_path):
        messagebox.showerror("Error", "This path does not exist!")
        return

    if not os.path.isdir(file_path):
        messagebox.showerror("Error", "This is not a folder path!!!")
        return

    files = os.listdir(file_path)
    if not files:
        messagebox.showinfo("Error", "The folder is empty!!!")
        return

    files.sort()

    # --- Input logic ---
    while True:
        new_name = simpledialog.askstring("Enter name", "Enter a name for the files:")
        if new_name is None:
            sys.exit()

        if new_name is not None and new_name != "":
            # User entered name - business as usual
            break
        elif new_name == "" or new_name is None:
            # User entered Enter without name
            choice = simpledialog.askstring(
                "Without a name",
                "You did not enter a name.\n"
                "The files will simply be numbered '1, 2...'"
                "Press Enter to continue or R to retype the name!!!"
            )

            if choice is None or choice == "":
                # Just Enter → numbering files
                new_name = ""
                break
            elif choice.lower() == "r":
                # R → Asking for the name again
                continue
            else:
                # Any other character → exit
                messagebox.showinfo("The program was completed", f"You entered '{choice}', the program was completed!")
                return

    # --- File naming ---
    count = 0
    for file in files:
        if os.path.isdir(os.path.join(file_path, file)):
            continue
        if file.startswith("."):
            continue

        old_path = os.path.join(file_path, file)
        ext = os.path.splitext(file)[1]
        new_file_name = f"{new_name}_{count + 1}{ext}" if new_name else f"{count + 1}{ext}"
        new_path = os.path.join(file_path, new_file_name)
        os.rename(old_path, new_path)
        count += 1

    messagebox.showinfo("Done", f"Renamed {count} files")


# --- GUI ---
root = tk.Tk()
root.title("Renaming files")
root.geometry("400x150")

btn = tk.Button(root, text="Select a folder and rename files", command=rename_files)
btn.pack(expand=True, pady=50)

root.mainloop()
