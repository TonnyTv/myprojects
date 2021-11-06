import errno, os, json, shutil
from tkinter import *
from tkinter import ttk, filedialog, messagebox


root = Tk()
root.title("OrdenaMaster")

with open('ext.json') as json_file:
    ext_main = json.load(json_file)



def ordenar(archivo, ext):
    if texto.get() == True:
        try:
            os.mkdir(dir_ord.get() + "/Texto")
        except OSError as e:
           if e.errno != errno.EEXIST:
               raise
        for i in ext_main['texto']:
            if ext == i:
                shutil.move(dir_ord.get() +"/" + archivo, dir_ord.get() + "/Texto")

    if imagen.get() == True:
        try:
            os.mkdir(dir_ord.get() + "/Imagenes")
        except OSError as e:
           if e.errno != errno.EEXIST:
               raise
        for i in ext_main['imagenes']:
            if ext == i:
                shutil.move(dir_ord.get() + "/" + archivo,
                            dir_ord.get() + "/Imagenes")
 
    if pdf.get() == True:
        try:
            os.mkdir(dir_ord.get() + "/PDF")
        except OSError as e:
           if e.errno != errno.EEXIST:
               raise
        for i in ext_main['pdf']:
            if ext == i:
                shutil.move(dir_ord.get() + "/" + archivo,
                            dir_ord.get() + "/PDF")

    if video.get() == True:
        try:
            os.mkdir(dir_ord.get() + "/Videos")
        except OSError as e:
           if e.errno != errno.EEXIST:
               raise
        for i in ext_main['video']:
            if ext == i:
                shutil.move(dir_ord.get() + "/" + archivo,
                            dir_ord.get() + "/Videos")

    if excel.get() == True:
        try:
            os.mkdir(dir_ord.get() + "/Excel")
        except OSError as e:
           if e.errno != errno.EEXIST:
               raise
        for i in ext_main['excel']:
            if ext == i:
                shutil.move(dir_ord.get() + "/" + archivo,
                            dir_ord.get() + "/Excel")

    if compress.get() == True:
        try:
            os.mkdir(dir_ord.get() + "/Comprimido")
        except OSError as e:
           if e.errno != errno.EEXIST:
               raise
        for i in ext_main['comprimido']:
            if ext == i:
                shutil.move(dir_ord.get() + "/" + archivo,
                            dir_ord.get() + "/Comprimido")



def iniciar():
    print(dir_ord.get())
    for archivo in os.listdir(dir_ord.get()):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(archivo, ext)
    
    messagebox.showinfo("Terminado", "Tutorial completado, bitches")

def carpeta():
    dir = filedialog.askdirectory()
    print(dir)
    if dir != None:
        ttk.Label(mainframe, text=dir).grid(
            row=2, column=1)
    else:
        pass
    
    return dir_ord.set(dir)


def pdfScript():
    print(pdf.get())

mainframe = ttk.Frame(root, padding =( "10 15 15 10"))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Selecciona la carpeta donde quieres ordenar tus archivos").grid(
    row=0, column=0, columnspan=3, sticky=(N, W, E, S))
dir_ord = StringVar()
ttk.Button(mainframe, text="Seleccionar carpeta", command=carpeta).grid(row=1, column=1,)

texto = BooleanVar()
ttk.Checkbutton(mainframe, text='Texto', 
	     variable=texto).grid(column=0, row=4)
imagen = BooleanVar()
ttk.Checkbutton(mainframe, text='Imagen',
                variable=imagen).grid(column=1, row=4)
pdf = BooleanVar()
ttk.Checkbutton(mainframe, text='PDF',
                variable=pdf, command=pdfScript).grid(column=2, row=4)
video = BooleanVar()
ttk.Checkbutton(mainframe, text='Videos',
                variable=video).grid(column=0, row=5)
excel = BooleanVar()
ttk.Checkbutton(mainframe, text='Excel',
                variable=excel).grid(column=1, row=5)
compress = BooleanVar()
ttk.Checkbutton(mainframe, text='Comprimido',
                variable=compress).grid(column=2, row=5)

ttk.Button(mainframe, text="Ordenar Archivos", command=iniciar).grid(column=2, row= 6)



root.mainloop()
