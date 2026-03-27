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

