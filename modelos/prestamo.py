from datetime import date


class Prestamo:
    def __init__(self, socio, libro):
        self.__socio = socio
        self.__libro = libro
        self.__fecha = date.today()
        self.__activo = True
        libro.prestar()

    def get_socio(self):
        return self.__socio

    def get_libro(self):
        return self.__libro

    def esta_activo(self):
        return self.__activo

    def finalizar(self):
        self.__activo = False
        self.__libro.devolver()

    def mostrar_datos(self):
        return self.__libro.get_titulo() + " - " + self.__socio.get_nombre() + " - " + str(self.__fecha)