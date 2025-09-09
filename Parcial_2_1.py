import tkinter as tk
from tkinter import messagebox

class CandidatasV:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Candidatas - Quetzaltenango")
        self.ventana.geometry("600x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Candidatas\n Reina de independencia 2025- Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Registrar candidata", command=self.inscribir_candidata)
        opciones.add_command(label="Registrar Jurados", command=self.registrar_jurado)
        opciones.add_command(label="Registrar Calificaciones", command=self.registrar_calificaciones)
        opciones.add_command(label="Calculo de promedio", command=self.Calculo_Promedio)
        opciones.add_command(label="Mostrar Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_candidata(self):
        win = tk.Toplevel(self.ventana)
        win.title("Inscribir Candidata")
        win.geometry("350x300")
        tk.Label(win, text="Código:").pack()
        codigo = tk.Entry(win)
        codigo.pack()
        tk.Label(win, text="Nombre:").pack()
        nombre = tk.Entry(win)
        nombre.pack()
        tk.Label(win, text="Edad:").pack()
        edad = tk.Entry(win)
        edad.pack()
        tk.Label(win, text="Institución Educativa:").pack()
        institucion = tk.Entry(win)
        institucion.pack()
        tk.Label(win, text="Municipio:").pack()
        municipio = tk.Entry(win)
        municipio.pack()

        def guardar():
            if not codigo.get() or not nombre.get() or not edad.get() or not institucion.get() or not municipio.get():
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            messagebox.showinfo("Éxito", f"Candidata '{nombre.get()}' registrada correctamente.")
            win.destroy()

        tk.Button(win, text="Registrar", command=guardar).pack(pady=10)

    