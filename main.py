import os
from tkinter import*
from tkinter import filedialog,colorchooser,font
from tkinter.messagebox import*
from tkinter.filedialog import*

def colour_change():
    colour = colorchooser.askcolor(title="Choose you colour")
    text_area.config(fg=colour[1]) # We wrote the index because when we print colour, we get a tuple of RGB and
                                   # Hexadecimal value. So index 1 will give us the hexadecimal and print it

def font_change(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0,END)

def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),
                                   ("Text documents","*.txt")])

    if not file:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file,"w")

            file.write(text_area.get(1,END))
        except Exception:
            print("File has been saved")

def open_file():
    file = askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file.name))
        text_area.delete(1.0, END)  # Use 1.0 to delete from the beginning
        text_area.insert(INSERT, file.read())
    except Exception:
        print("Couldn't open file")
    finally:
        file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("Welcome to the text editor","This is a simple text editor using which you can type anything. You can save"
             " the text file. You can choose the colour, font, and font size that you want")

def quit():
    window.destroy()

window = Tk()
window.title("Text editor")

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

font_name = StringVar(window)
font_name.set("Arial")

font_size= StringVar(window)
font_size.set("25")

text_area = Text(window,font=(font_name.get(),font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + S + E + W)

scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

font_box = OptionMenu(frame,font_name,*font.families(),command=colour_change)
font_box.grid(row=0,column=1)

colour_button = Button(frame,command=colour_change,text="Colour chooser")
colour_button.grid(row=0,column=0)

size_box = Spinbox(frame,from_=1,to=100,textvariable= font_size,command=font_change)
size_box.grid(row=0,column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=quit)

edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)

help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About",command=about)

window.mainloop()

