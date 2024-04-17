from tkinter import *
from tkinter import filedialog
from tkinter import font


# Create the window
root = Tk()
root.title("TextPad Application")
root.geometry("1200x600+50+2")

global file_name_exist
file_name_exist = False
# ==================================Functions===========================
# Function To create New File
def new_file():
    # Delete All the text In the TextBox
    text_box.delete("1.0", END) 
    # Changes the title Of the window
    root.title("New File - TextPad")
    # Changes the text on the status from ready to New File
    status_bar.config(text="New File       ")
    global file_name_exist
    file_name_exist = False

# Function To Open File directory
def open_file():
    # Delete the previous Text On the TextBox
    text_box.delete("1.0", END)
    # Open The File directory
    text_file = filedialog.askopenfilename(initialdir=r"C:\Users\Flivian\PROJECTS", title="Open File", filetypes=(("Text Files","*.text"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    # Checks if the file name exist
    if text_file:
        # Make file Name Global variable
        global file_name_exist
        file_name_exist = text_file
    name = text_file
    # Updates The Status Bar and the main Window Title
    status_bar.config(text=f"{name}       ")
    name = name.replace("C:/Users/Flivian/PROJECTS", "")
    root.title(f"{name} - TextPad")
    # Open the file on the Textbox
    text_file = open(text_file, "r")
    stuff = text_file.read()
    # Add the file on the textBox
    text_box.insert(END, stuff)
    # Close the Open file
    text_file.close()

# Function To save file as
def save_as_file():
    # Open the file directory
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir=r"C:\Users\Flivian\PROJECTS", title="Open File", filetypes=(("Text Files","*.text"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f"Saved {name}       ")
        name = name.replace("C:/Users/Flivian/PROJECTS/", "")
        root.title(f"{name} - TextPad")
        # Save file To the currecnt directory
        text_file = open(text_file, "w")
        text_file.write(text_box.get("1.0", END))
        # close the Save file
        text_file.close()

def save_file():
    global file_name_exist
    if file_name_exist:
        # Save file To the currecnt directory
        text_file = open(file_name_exist, "w")
        text_file.write(text_box.get("1.0", END))
        # close the Save file
        text_file.close()
        status_bar.config(text=f"Saved {file_name_exist}       ")
    else:
        save_as_file()
        
    



# Create A Main Frame
frame = Frame(root)
frame.pack(pady=5)

# Creatae A Scroll Bar
y_scroll = Scrollbar(frame)
y_scroll.pack(side=RIGHT, fill=Y)

# Create A texBox
text_box = Text(frame,width=107, height=24,selectbackground="green", selectforeground="black", undo=True, font=("Bookman Old Style", 15), yscrollcommand=y_scroll.set)
text_box.pack()

# Configure the scroll Bar
y_scroll.config(command=text_box.yview)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add file Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Status Bar on the bottom
status_bar = Label(root, text="Ready            ", anchor=E, font=("Bookman Old Style",12,"bold"))
status_bar.pack(fill=X, side=BOTTOM, ipadx=10, ipady=5)

root.mainloop()