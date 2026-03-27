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
    
    def listar_tareas(self) -> list:
        """
        Retorna una copia de la lista de tareas.
        """
        return self._lista_tareas.copy()

    def buscar_tarea_por_identificador(self, identificador: int):
        """
        Busca una tarea por su identificador.
        Retorna la tarea si existe o None si no se encuentra.
        """
        for tarea in self._lista_tareas:
            if tarea.identificador == identificador:
                return tarea
        return None
 
    
