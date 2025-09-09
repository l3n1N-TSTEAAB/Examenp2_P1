import tkinter as tk
from tkinter import messagebox

class CandidatasTxt:
    def __init__(self):
        self.candidatas = {}
        self.cargar_candidatas()

    def cargar_candidatas(self):
        try:
            with open("candidatas.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, edad, institucion, municipio = linea.split(":")
                        self.candidatas[codigo] = {
                            "Nombre": nombre,
                            "Edad": edad,
                            "Institucion": institucion,
                            "Municipio": municipio
                        }
            print("Candidatas importadas desde candidatas.txt")
        except FileNotFoundError:
            print("No existe el archivo candidatas.txt, se creará uno nuevo al guardar.")

    def guardar_candidatas(self):
        with open("candidatas.txt", "w", encoding="utf-8") as archivo:
            for codigo, datos in self.candidatas.items():
                archivo.write(f"{codigo}:{datos['Nombre']}:{datos['Edad']}:{datos['Institucion']}:{datos['Municipio']}\n")

    def agregar_candidata(self, codigo, nombre, edad, institucion, municipio):
        self.candidatas[codigo] = {
            "Nombre": nombre,
            "Edad": edad,
            "Institucion": institucion,
            "Municipio": municipio
        }
        self.guardar_candidatas()
        print(f"Candidata con código {codigo} agregada y guardada correctamente.")

class JuradosTxt:
    def __init__(self):
        self.jurados = {}
        self.cargar_jurados()

    def cargar_jurados(self):
        try:
            with open("jurados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_jurado, nombre, profesion = linea.split(":")
                        self.jurados[id_jurado] = {
                            "Nombre": nombre,
                            "Profesion": profesion
                        }
            print("Jurados importados desde jurados.txt")
        except FileNotFoundError:
            print("No existe el archivo jurados.txt, se creará uno nuevo al guardar.")

    def guardar_jurados(self):
        with open("jurados.txt", "w", encoding="utf-8") as archivo:
            for id_jurado, datos in self.jurados.items():
                archivo.write(f"{id_jurado}:{datos['Nombre']}:{datos['Profesion']}\n")

    def agregar_jurado(self, id_jurado, nombre, profesion):
        self.jurados[id_jurado] = {
            "Nombre": nombre,
            "Profesion": profesion
        }
        self.guardar_jurados()
        print(f"Jurado con ID {id_jurado} agregado y guardado correctamente.")


class CalificacionesTxt:
    def __init__(self):
        self.calificaciones = []
        self.cargar_calificaciones()

    def cargar_calificaciones(self):
        try:
            with open("calificaciones.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        cultura, proyeccion, entrevista = linea.split(":")
                        self.calificaciones.append({
                            "Cultura": cultura,
                            "Proyeccion": proyeccion,
                            "Entrevista": entrevista
                        })
            print("Calificaciones importadas desde calificaciones.txt")
        except FileNotFoundError:
            print("No existe el archivo calificaciones.txt, se creará uno nuevo al guardar.")

    def guardar_calificaciones(self):
        with open("calificaciones.txt", "w", encoding="utf-8") as archivo:
            for datos in self.calificaciones:
                archivo.write(f"{datos['Cultura']}:{datos['Proyeccion']}:{datos['Entrevista']}\n")

    def agregar_calificacion(self, cultura, proyeccion, entrevista):
        self.calificaciones.append({
            "Cultura": cultura,
            "Proyeccion": proyeccion,
            "Entrevista": entrevista
        })
        self.guardar_calificaciones()
        print("Calificación agregada y guardada correctamente.")


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

