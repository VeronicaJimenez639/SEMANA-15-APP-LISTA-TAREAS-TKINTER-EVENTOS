import tkinter as tk
from tkinter import ttk, messagebox

from servicios.tarea_servicio import TareaServicio


class AppTkinter:
    """
    Interfaz gráfica principal de la aplicación.
    Aquí se construyen los widgets y se capturan los eventos del usuario.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Se cambia el tema visual de ttk para que el Treeview sí permita mostrar
        # los colores personalizados de las filas en Windows.
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")

        # Se crea la instancia del servicio para manejar la lógica de las tareas.
        self.tarea_servicio = TareaServicio()

        # Esta variable almacena el texto que el usuario escribe en el Entry.
        self.descripcion_var = tk.StringVar()

        self.crear_componentes()
        self.configurar_eventos()

    def crear_componentes(self):
        """
        Crea y organiza los elementos visuales de la ventana.
        """
        frame_superior = ttk.Frame(self.root, padding=10)
        frame_superior.pack(fill="x")

        etiqueta_descripcion = ttk.Label(frame_superior, text="Descripción de la tarea:")
        etiqueta_descripcion.pack(anchor="w", pady=(0, 5))

        self.entry_descripcion = ttk.Entry(
            frame_superior,
            textvariable=self.descripcion_var,
            width=60
        )
        self.entry_descripcion.pack(fill="x", pady=(0, 10))
        self.entry_descripcion.focus()

        frame_botones = ttk.Frame(frame_superior)
        frame_botones.pack(fill="x", pady=(0, 10))

        self.boton_anadir_tarea = ttk.Button(
            frame_botones,
            text="Añadir Tarea",
            command=self.anadir_tarea
        )
        self.boton_anadir_tarea.pack(side="left", padx=(0, 10))

        self.boton_marcar_completada = ttk.Button(
            frame_botones,
            text="Marcar Completada",
            command=self.marcar_tarea_completada
        )
        self.boton_marcar_completada.pack(side="left", padx=(0, 10))

        self.boton_desmarcar_tarea = ttk.Button(
            frame_botones,
            text="Desmarcar Tarea",
            command=self.desmarcar_tarea
        )
        self.boton_desmarcar_tarea.pack(side="left", padx=(0, 10))

        self.boton_eliminar_tarea = ttk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar_tarea
        )
        self.boton_eliminar_tarea.pack(side="left")

        frame_lista = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        frame_lista.pack(fill="both", expand=True)

        self.treeview_tareas = ttk.Treeview(
            frame_lista,
            columns=("descripcion", "estado"),
            show="headings",
            height=14
        )
        self.treeview_tareas.heading("descripcion", text="Descripción")
        self.treeview_tareas.heading("estado", text="Estado")
        self.treeview_tareas.column("descripcion", width=460)
        self.treeview_tareas.column("estado", width=180, anchor="center")
        self.treeview_tareas.pack(fill="both", expand=True)

        # Estas etiquetas visuales permiten diferenciar tareas pendientes y completadas.
        # También se define el color del texto para que se vea con más claridad.
        self.treeview_tareas.tag_configure("pendiente", background="#FFF9C4", foreground="black")
        self.treeview_tareas.tag_configure("completada", background="#C8E6C9", foreground="black")

    def configurar_eventos(self):
        """
        Registra los eventos de teclado y ratón.
        """
        # Permite agregar una tarea al presionar Enter en el campo de texto.
        self.entry_descripcion.bind("<Return>", self.evento_anadir_con_enter)

        # Permite marcar una tarea como completada con doble clic.
        self.treeview_tareas.bind("<Double-1>", self.evento_marcar_con_doble_clic)

    def anadir_tarea(self):
        """
        Toma el texto escrito por el usuario y crea una nueva tarea.
        """
        descripcion_ingresada = self.descripcion_var.get().strip()

        if not descripcion_ingresada:
            messagebox.showwarning("Aviso", "Debe escribir una descripción para la tarea.")
            self.entry_descripcion.focus()
            return

        try:
            tarea_nueva = self.tarea_servicio.agregar_tarea(descripcion_ingresada)
            self.insertar_tarea_en_treeview(tarea_nueva)
            self.descripcion_var.set("")
            self.entry_descripcion.focus()
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def insertar_tarea_en_treeview(self, tarea):
        """
        Inserta una tarea en el Treeview.
        El identificador se guarda como iid para poder ubicar la tarea después.
        """
        estado_texto = "Pendiente"
        etiquetas = ("pendiente",)

        if tarea.estado_completado:
            estado_texto = "[Hecho]"
            etiquetas = ("completada",)

        self.treeview_tareas.insert(
            "",
            "end",
            iid=str(tarea.identificador),
            values=(tarea.descripcion, estado_texto),
            tags=etiquetas
        )

    def obtener_identificador_seleccionado(self):
        """
        Obtiene el identificador de la tarea seleccionada.
        Retorna None si no hay ninguna seleccionada.
        """
        seleccion = self.treeview_tareas.selection()

        if not seleccion:
            return None

        return int(seleccion[0])
    
