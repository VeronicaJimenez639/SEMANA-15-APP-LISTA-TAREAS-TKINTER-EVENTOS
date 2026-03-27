from modelos.tarea import Tarea


class TareaServicio:
    """
    Gestiona la lógica de negocio de las tareas.
    Aquí se agregan, buscan, completan y eliminan tareas.
    """

    def __init__(self):
        self._lista_tareas = []
        self._siguiente_identificador = 1

    def agregar_tarea(self, descripcion: str) -> Tarea:
        """
        Crea una nueva tarea, la guarda en memoria y la retorna.
        """
        nueva_tarea = Tarea(self._siguiente_identificador, descripcion)
        self._lista_tareas.append(nueva_tarea)
        self._siguiente_identificador += 1
        return nueva_tarea
    
