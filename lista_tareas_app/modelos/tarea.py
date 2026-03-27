class Tarea:
    """
    Representa una tarea dentro de la aplicación.
    Se usa property para aplicar encapsulamiento y validaciones.
    """

    def __init__(self, identificador: int, descripcion: str, estado_completado: bool = False):
        self.identificador = identificador
        self.descripcion = descripcion
        self.estado_completado = estado_completado

    @property
    def identificador(self) -> int:
        return self._identificador

    @identificador.setter
    def identificador(self, value: int):
        # Validamos que el identificador sea un número entero positivo.
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El identificador debe ser un entero positivo.")
        self._identificador = value

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: str):
        # Validamos que la descripción no esté vacía.
        if not value or not value.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = value.strip()

    @property
    def estado_completado(self) -> bool:
        return self._estado_completado

    @estado_completado.setter
    def estado_completado(self, value: bool):
        # Validamos que el estado sea verdadero o falso.
        if not isinstance(value, bool):
            raise ValueError("El estado completado debe ser booleano.")
        self._estado_completado = value