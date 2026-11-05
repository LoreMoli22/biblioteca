class Libro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponible = True

    def get_titulo(self):
        return self.__titulo

    def get_codigo(self):
        return self.__codigo

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def mostrar_datos(self):
        if self.__disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
        return self.__titulo + " - " + self.__autor + " (" + estado + ")"