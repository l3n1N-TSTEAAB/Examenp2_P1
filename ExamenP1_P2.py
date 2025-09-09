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