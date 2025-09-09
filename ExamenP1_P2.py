import tkinter as tk

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
        print("Se abrió la ventana: Inscribir Candidata")
        tk.Toplevel(self.ventana).title("Inscribir Candidata")

    def registrar_jurado(self):
        print("Se abrió la ventana: Registrar Jurados")
        tk.Toplevel(self.ventana).title("Registrar Jurados")

    def registrar_calificaciones(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Registro-calificaciones")

    def Calculo_Promedio(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Promedio")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    CandidatasV()


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


        candidata = Candidatas(codigo,nombre,institucionE,municipio)
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
        self.Puntajes[culturaGen] = puntajes
        print("Puntaje registrado exitosamente")

