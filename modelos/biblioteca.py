from modelos.prestamo import Prestamo


class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []
        self.__socios = []
        self.__prestamos = []

    def get_nombre(self):
        return self.__nombre

    def agregar_libro(self, libro):
        if self.buscar_libro(libro.get_isbn()) is not None:
            return False
        self.__libros.append(libro)
        return True

    def agregar_socio(self, socio):
        if self.buscar_socio(socio.get_numero_socio()) is not None:
            return False
        self.__socios.append(socio)
        return True

    def buscar_libro(self, isbn):
        for libro in self.__libros:
            if libro.get_isbn() == isbn:
                return libro
        return None

    def buscar_socio(self, numero):
        for socio in self.__socios:
            if socio.get_numero_socio() == numero:
                return socio
        return None

    def buscar_por_titulo(self, texto):
        resultado = []
        for libro in self.__libros:
            if texto.lower() in libro.get_titulo().lower():
                resultado.append(libro)
        return resultado

    def prestar(self, numero_socio, isbn):
        socio = self.buscar_socio(numero_socio)
        libro = self.buscar_libro(isbn)
        if socio is None or libro is None:
            return "Socio o libro inexistente"
        if not libro.esta_disponible():
            return "El libro no esta disponible"
        prestamo = Prestamo(socio, libro)
        self.__prestamos.append(prestamo)
        return "Prestamo registrado"

    def devolver(self, isbn):
        for prestamo in self.__prestamos:
            if prestamo.esta_activo() and prestamo.get_libro().get_isbn() == isbn:
                prestamo.finalizar()
                return "Devolucion registrada"
        return "Ese libro no tiene un prestamo activo"

    def get_libros(self):
        return self.__libros

    def get_prestamos_activos(self):
        activos = []
        for prestamo in self.__prestamos:
            if prestamo.esta_activo():
                activos.append(prestamo)
        return activos