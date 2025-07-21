import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog


# === FUNCIONES ===

def buscar_archivo():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, file_path)

def corromper_archivo():
    ruta = entry_archivo.get()
    if not os.path.exists(ruta) or ruta.strip() == "":
        messagebox.showerror("¡ERROR!", f"El archivo no fue encontrado...\n¿Estás seguro de lo que haces?")
        return

    try:
       

        with open(ruta, 'rb') as archivo:
            contenido = bytearray(archivo.read())

        tamano = len(contenido)
        pasadas = int(spin_pasadas.get())
        
        
        for _ in range(pasadas):
            for _ in range(tamano + 100):
                i = random.randint(0, tamano - 1)
                contenido[i] = random.randint(0, 255)

        with open(ruta, 'wb') as archivo:
            archivo.write(contenido)

        messagebox.showinfo("¡CORRUPCIÓN COMPLETA!", f"Tu archivo ha sido condenado... 😈\n")
       
        if messagebox.askokcancel("Borrado del archivo",f"QUIERES QUE DESAPARESCA?... {ruta}"):
           os.remove(ruta)
           entry_archivo.delete(first=0,last=tk.END)
        else:
            messagebox.showinfo("¡LOCALIZACION DE ARCHIVO!", f"Tu archivo esta en {ruta} \n")
            entry_archivo.delete(first=0,last=tk.END)
        
    except Exception as e:
        messagebox.showerror("¡ALGO SALIÓ MAL!", str(e))

# === INTERFAZ ===

ventana = tk.Tk()
ventana.title("Corruptor Maldito 👁️‍🗨️")
ventana.geometry("520x240")
ventana.configure(bg="#1a1a1a")
ventana.resizable(False, False)

# === Estilo de miedo ===
fuente_titulo = ("Courier New", 18, "bold")
fuente_normal = ("Courier New", 10)

# Título
titulo = tk.Label(ventana, text="👁️‍🗨️ Corruptor de Archivos Prohibidos 👁️‍🗨️", font=fuente_titulo, bg="#1a1a1a", fg="#ff4d4d")
titulo.pack(pady=10)

# Campo de archivo
frame_archivo = tk.Frame(ventana, bg="#1a1a1a")
frame_archivo.pack(pady=5)

entry_archivo = tk.Entry(frame_archivo, width=45, font=fuente_normal, bg="#333", fg="#f5f5f5", insertbackground="#f5f5f5")
entry_archivo.pack(side="left", padx=5)

btn_buscar = tk.Button(frame_archivo, text="Buscar...", command=buscar_archivo, bg="#660000", fg="white", font=fuente_normal)
btn_buscar.pack(side="left")

# Spinbox de pasadas
frame_pasadas = tk.Frame(ventana, bg="#1a1a1a")
frame_pasadas.pack(pady=10)

label_pasadas = tk.Label(frame_pasadas, text="Número de rituales (pasadas):", font=fuente_normal, bg="#1a1a1a", fg="#e6e6e6")
label_pasadas.pack(side="left", padx=5)

spin_pasadas = tk.Spinbox(frame_pasadas, from_=3, to=10, width=5, font=fuente_normal, bg="#333", fg="#f5f5f5", justify="center")
spin_pasadas.pack(side="left")

# Botón de corromper
btn_corromper = tk.Button(ventana, text="🔥 Invocar la Corrupción 🔥", command=corromper_archivo,
                          font=fuente_normal, bg="#8b0000", fg="white", padx=10, pady=5)
btn_corromper.pack(pady=15)

# Frase espeluznante
frase = tk.Label(ventana, text="Advertencia: No todos los archivos regresan del abismo intactos...",
                 font=("Courier", 8, "italic"), bg="#1a1a1a", fg="#999999")
frase.pack()

ventana.mainloop()
