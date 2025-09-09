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
        def cargar_calificaciones(self):
            try:
                with open("calificaciones.txt", "r", encoding="utf-8") as archivo:
                    for linea in archivo:
                        linea = linea.strip()
                        if linea:
                            partes = linea.split(":")
                            if len(partes) != 4:
                                print(f"Línea inválida ignorada: {linea}")
                                continue
                            codigo, cultura, proyeccion, entrevista = partes
                            self.calificaciones.append({
                                "Codigo": codigo,
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
                archivo.write(f"{datos['Codigo']}:{datos['Cultura']}:{datos['Proyeccion']}:{datos['Entrevista']}\n")

    def agregar_calificacion(self, codigo_candidata, cultura, proyeccion, entrevista):
        self.calificaciones.append({
            "Codigo": codigo_candidata,
            "Cultura": cultura,
            "Proyeccion": proyeccion,
            "Entrevista": entrevista
        })
        self.guardar_calificaciones()
        print(f"Calificación para candidata {codigo_candidata} agregada correctamente.")



class CandidatasV:
    def __init__(self):

        self.candidatas_txt = CandidatasTxt()
        self.jurados_txt = JuradosTxt()
        self.calificaciones_txt = CalificacionesTxt()


        self.ventana = tk.Tk()
        self.ventana.title("Candidatas - Quetzaltenango")
        self.ventana.geometry("600x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Candidatas\n",
            font=("Arial", 15,"bold",),
            foreground="blue",
            relief="sunken",
            borderwidth=5,
            justify="center"
        ).pack(pady=50)
        tk.Label(
            self.ventana,
            text = "Reina de independencia 2025- Quetzaltenango",
            font = ("Arial", 15, "bold",),
            foreground = "red",
            relief = "sunken",
            borderwidth = 10,
            justify = "center"
        ).pack(pady=1)


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

                # Guardar en candidatas.txt
                self.candidatas_txt.agregar_candidata(
                    codigo.get(), nombre.get(), edad.get(), institucion.get(), municipio.get()
                )

                messagebox.showinfo("Éxito", f"Candidata '{nombre.get()}' registrada correctamente.")
                win.destroy()

        tk.Button(win, text="Registrar", command=guardar).pack(pady=10)
        tk.Button(win, text="Regresar", command=win.destroy).pack(pady=10)

    def registrar_jurado(self):
        win1 = tk.Toplevel(self.ventana)
        win1.title("Inscribir Jurados")
        win1.geometry("350x300")
        tk.Label(win1, text="Id Jurado:").pack()
        IdJurado = tk.Entry(win1)
        IdJurado.pack()
        tk.Label(win1, text="Nombre de Jurado:").pack()
        NombreJ = tk.Entry(win1)
        NombreJ.pack()
        tk.Label(win1, text="Profesion:").pack()
        profesion = tk.Entry(win1)
        profesion.pack()

        def guardar():
            if not IdJurado.get() or not NombreJ.get() or not profesion.get():
                messagebox.showerror("Error",   "Todos los campos son obligatorios.")
                return

            self.jurados_txt.agregar_jurado(
                IdJurado.get(),
                NombreJ.get(),
                profesion.get()
            )
            messagebox.showinfo("Éxito", f"Jurado '{NombreJ.get()}' registrado correctamente.")
            win1.destroy()

        tk.Button(win1, text="Registrar", command=guardar).pack(pady=10)
        tk.Button(win1, text="Regresar", command=win1.destroy).pack(pady=10)


    def registrar_calificaciones(self):
        win2 = tk.Toplevel(self.ventana)
        win2.title("REGISTRO DE CANDIDATAS")
        win2.geometry("350x300")

        tk.Label(win2, text="Codigo de candidata:").pack()
        codigo = tk.Entry(win2)
        codigo.pack()

        tk.Label(win2, text="Criterio Cultural General:").pack()
        culturaGen = tk.Entry(win2)
        culturaGen.pack()
        tk.Label(win2, text="Criterio de proyeccion:").pack()
        Proyeccion = tk.Entry(win2)
        Proyeccion.pack()
        tk.Label(win2, text="Criterio de entrevista:").pack()
        Entrevista = tk.Entry(win2)
        Entrevista.pack()

        def guardarCal():
            if not codigo.get() or not culturaGen.get() or not Proyeccion.get() or not Entrevista.get():
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            self.calificaciones_txt.agregar_calificacion(
                codigo.get(),
                culturaGen.get(),
                Proyeccion.get(),
                Entrevista.get()
            )
            messagebox.showinfo("Éxito", f"Criterios registrados correctamente.")
            win2.destroy()

        tk.Button(win2, text="Registrar", command=guardarCal).pack(pady=10)
        tk.Button(win2, text="Regresar", command=win2.destroy).pack(pady=10)

    def Calculo_Promedio(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Promedio")

    def ver_ranking(self):
            win3 = tk.Toplevel(self.ventana)
            win3.title("Ranking Final")
            win3.geometry("400x400")

            resultados = []
            for cal in self.calificaciones_txt.calificaciones:
                codigo = cal["Codigo"]
                if codigo in self.candidatas_txt.candidatas:
                    candidata = self.candidatas_txt.candidatas[codigo]

                    try:
                        cultura = int(cal["Cultura"])
                        proyeccion = int(cal["Proyeccion"])
                        entrevista = int(cal["Entrevista"])
                    except ValueError:
                        continue

                    promedio = (cultura + proyeccion + entrevista) / 3

                    resultados.append({
                        "Codigo": codigo,
                        "Nombre": candidata["Nombre"],
                        "Edad": candidata["Edad"],
                        "Institucion": candidata["Institucion"],
                        "Municipio": candidata["Municipio"],
                        "Promedio": promedio,
                    })

            # Ordenar de mayor a menor promedio
            resultados.sort(key=lambda x: x["Promedio"], reverse=True)

            tk.Label(win3, text="Ranking Final", font=("Arial", 14, "bold")).pack(pady=10)

            if not resultados:
                tk.Label(win3, text="No hay resultados registrados.", font=("Arial", 12)).pack(pady=20)
                return

            for i, r in enumerate(resultados, start=1):
                texto = (f"{i}. {r['Nombre']} ({r['Codigo']}) - "
                         f"{r['Edad']} años - {r['Institucion']} - {r['Municipio']} "
                         f"| Promedio: {r['Promedio']:.2f}")
                tk.Label(win3, text=texto, font=("Arial", 11), anchor="w").pack(fill="x", padx=10, pady=3)
class Candidatas:
    def __init__(self,codigo,nombre,edad,institucionE,municipio):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.institucionE = institucionE
        self.municipio = municipio


    def MostrarCanditas(self):
        print(f"CODIGO: {self.codigo} + Nombre: {self.nombre} + Edad:{self.edad}+ INSTITUCION: {self.institucionE}+ Municipio: {self.municipio}")


class RegistroCandidatas:
    def __init__(self):
        self.Candidatas = {}

    def AgregarCandidatas(self):
        while True:
            codigo = input("Ingrese código de candidata: ").strip()
            if not codigo:
                print("Error: El código no puede estar vacío.\n")
                continue
            if codigo in self.Candidatas:
                print(f"Error: El código '{codigo}' ya está registrado.\n")
                continue
            break

        while True:
            nombre = input("Ingrese nombre de la candidata: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío.\n")
                continue
            break
        while True:
            edad = input("Ingrese edad: ").strip()
            if not edad:
                print("Error: La edad no puede estar vacía.\n")
        while True:
            institucionE = input("Ingrese la institucion de la candidata: ").strip()
            if not institucionE:
                print("Error: El nombre no puede estar vacío.\n")
                continue
            break

        while True:
            municipio = input("Ingrese la municipio del candidata: ").strip()
            if not municipio:
                print("Error: El municipio no puede estar vacío\n")
                continue
            break


        candidata = Candidatas(codigo,nombre,edad,institucionE,municipio)
        self.Candidatas[codigo] = candidata
        print("Candidata registrada automaticamente")


class Jurados:
    def __init__(self,IdJurado,NombreJ,Profesion):
        self.IdJurado = IdJurado
        self.NombreJ = NombreJ
        self.Profesion = Profesion


    def MostrarJurado(self):
        print(f"ID Jurado: {self.IdJurado} + Nombre: {self.NombreJ} + Profesion: {self.Profesion}")


class RegistrarJurados:
    def __init__(self):
        self.Jurados = {}

    def AgregarJurados(self):
            while True:
                IdJurado = input("Ingrese Id del jurado: ").strip()
                if not IdJurado:
                    print("Error: El Id no puede estar vacío.\n")
                    continue
                if IdJurado in self.Jurados:
                    print(f"Error: El código '{IdJurado}' ya está registrado.\n")
                    continue
                break

            while True:
                NombreJ = input("Ingrese nombre del jurado: ").strip()
                if not NombreJ:
                    print("Error: El nombre no puede estar vacío.\n")
                    continue
                break

            while True:
                profesion = input("Ingrese la profesion del jurado: ").strip()
                if not profesion:
                    print("Error: El nombre no puede estar vacío.\n")
                    continue
                break

            jurado = Jurados(IdJurado,NombreJ,profesion)
            self.Jurados[IdJurado] = jurado
            print("Jurado registrado automaticamente")

class Puntaje:
    def __init__(self,culturaGen,Proyeccion,Entrevista):
        self.culturaGen = culturaGen
        self.Proyeccion = Proyeccion
        self.Entrevista = Entrevista

class RegistrarPuntaje():
    def __init__(self):
        self.Puntajes = {}

    def AgregarPuntajes(self):
        while True:
            culturaGen = input("Criterio cultura general: ").strip()
            if not  culturaGen:
                print("Error: El criterio no puede estar vacio.\n")
                continue
            if  culturaGen in self.Puntajes:
                print(f"Error: El criterio '{culturaGen}' ya está registrado.\n")
                continue
            break

        while True:
            Proyeccion = input("Criterio Proyeccion escenica: ").strip()
            if not Proyeccion:
                print("Error: El criterio no puede estar vacío.\n")
                continue
            break

        while True:
            Entrevista = input("Criterio de entrevista: ").strip()
            if not Entrevista:
                print("Error: El nombre no puede estar vacío.\n")
                continue
            break

        puntajes = Puntaje(culturaGen,Proyeccion,Entrevista)
        self.Puntajes[len(self.Puntajes)+1] = puntajes
        print("Puntaje registrado exitosamente")

if __name__ == "__main__":
    CandidatasV()