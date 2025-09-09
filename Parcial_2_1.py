import os
import tkinter as tk
from tkinter import ttk, messagebox


def inscribir_Candidata(self):
    win = self._crear_toplevel("Inscribir Banda")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text="Codigo de la Candidata:").grid(row=0, column=0, sticky="w", pady=4)
    ttk.Label(frm, text="Nombre de la Candidata:").grid(row=0, column=0, sticky="w", pady=4)
    ttk.Label(frm, text="Edad de la Candidata:").grid(row=0, column=0, sticky="w", pady=4)
    ttk.Label(frm, text="Institucion:").grid(row=0, column=0, sticky="w", pady=4)
    ttk.Label(frm, text="Municipio:").grid(row=0, column=0, sticky="w", pady=4)

    v_nombre = tk.StringVar()
    v_inst = tk.StringVar()


    ttk.Entry(frm, textvariable=v_nombre, width=40).grid(row=0, column=1, pady=4, sticky="w")
    ttk.Entry(frm, textvariable=v_inst, width=40).grid(row=1, column=1, pady=4, sticky="w")
    ttk.Combobox(frm, textvariable=v_cat, values=CATEGORIAS_VALIDAS, state="readonly", width=20) \
        .grid(row=2, column=1, pady=4, sticky="w")

    def guardar():
        nombre = v_nombre.get().strip()
        inst = v_inst.get().strip()
        cat = v_cat.get().strip()
        if not nombre or not inst:
            messagebox.showwarning("Validación", "Nombre e institución son obligatorios.")
            return
        try:
            banda = BandaEscolar(nombre, inst, cat)
            self.concurso.inscribir_banda(banda)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return
