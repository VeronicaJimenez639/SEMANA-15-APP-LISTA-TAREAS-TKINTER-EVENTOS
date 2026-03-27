from modelos.tarea import Tarea


class TareaServicio:
    """
    Gestiona la lógica de negocio de las tareas.
    Aquí se agregan, buscan, completan y eliminan tareas.
    """

    def __init__(self):
        self._lista_tareas = []
        self._siguiente_identificador = 1