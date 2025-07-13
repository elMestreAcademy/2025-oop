import datetime


class Contacto:
    def __init__(self, nombre, apellido):
        self._creado = datetime.datetime.now()
        self._editado = self._creado
        self._editado_veces = 0
        self.popularidad = 0

        self._nombre = nombre
        self.apellido = apellido

    def __str__(self):
        msg = f"<{self.popularidad}> "
        msg += f"Nombre: {self.nombre.ljust(20)}  "
        msg += f"Apellido: {self.apellido.ljust(20)} "
        msg += f"creado: {self._creado} "
        msg += f"editado: {self._editado} {self._editado_veces} veces"

        return msg

    @property
    def nombre(self):
        self.popularidad += 1
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):

        # VALIDACIÓN
        nombre = nombre.capitalize()
        if not nombre.isalpha():
            raise ValueError('Los nombres deben formados por letras')

        # CONTROL a través de otros atributos
        self._editado_veces += 1
        self._editado = datetime.datetime.now()

        # FINALMENTE, guardamos el nombre
        self._nombre = nombre
