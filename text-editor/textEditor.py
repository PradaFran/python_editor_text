from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)

def saveFile():
    global filename
    if filename:
        t = text.get(1.0, END)
        with open(filename, 'w') as f:
            f.write(t)
    else:
        saveAs()

def saveAs():
    f = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if f is not None:
        t = text.get(1.0, END)
        try:
            f.write(t.rstrip())
        except:
            messagebox.showerror(title="Error", message="No es posible guardar el archivo")
        finally:
            f.close()

def openFile():
    global filename
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file is not None:
        filename = file.name
        text.delete(1.0, END)
        contents = file.read()
        text.insert(1.0, contents)
        file.close()

root = Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Nuevo", command=newFile)
filemenu.add_command(label="Abrir", command=openFile)
filemenu.add_command(label="Guardar", command=saveFile)
filemenu.add_command(label="Guardar como", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
