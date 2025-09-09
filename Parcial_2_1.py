def menu(self):
    barra = tk.Menu(self.ventana)
    opciones = tk.Menu(barra, tearoff=0)
    opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
    opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
    opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
    opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
    opciones.add_separator()
    opciones.add_command(label="Salir", command=self.ventana.quit)
    barra.add_cascade(label="Opciones", menu=opciones)
    self.ventana.config(menu=barra)


def _crear_toplevel(self, titulo: str, size: str = "560x420") -> tk.Toplevel:
    win = tk.Toplevel(self.ventana)
    win.title(titulo)
    win.geometry(size)
    win.grab_set()
    return win


def inscribir_banda(self):
    win = self._crear_toplevel("Inscribir Banda")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text="Nombre de la banda:").grid(row=0, column=0, sticky="w", pady=4)
    ttk.Label(frm, text="Institución:").grid(row=1, column=0, sticky="w", pady=4)
    ttk.Label(frm, text="Categoría:").grid(row=2, column=0, sticky="w", pady=4)

    v_nombre = tk.StringVar()
    v_inst = tk.StringVar()
    v_cat = tk.StringVar(value=CATEGORIAS_VALIDAS[0])

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

        # Guardar (reescribe archivos)
        AlmacenamientoTXT.guardar_bandas(self.concurso)
        AlmacenamientoTXT.guardar_evaluaciones(self.concurso)

        messagebox.showinfo("OK", f"Banda '{nombre}' inscrita.")
        win.destroy()

    btns = ttk.Frame(frm)
    btns.grid(row=10, column=0, columnspan=2, pady=10)
    ttk.Button(btns, text="Guardar", command=guardar).pack(side="left", padx=6)
    ttk.Button(btns, text="Cancelar", command=win.destroy).pack(side="left", padx=6)

    frm.columnconfigure(0, weight=0)
    frm.columnconfigure(1, weight=1)
