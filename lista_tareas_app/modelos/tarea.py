class Tarea:
    """
    Representa una tarea dentro de la aplicación.
    Se usa property para aplicar encapsulamiento y validaciones.
    """

    def __init__(self, identificador: int, descripcion: str, estado_completado: bool = False):
        self.identificador = identificador
        self.descripcion = descripcion
        self.estado_completado = estado_completado