class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    def get_titulo(self):
        return self.__titulo

    def get_isbn(self):
        return self.__isbn

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