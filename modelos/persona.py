class Persona:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def mostrar_datos(self):
        return "Nombre: " + self.__nombre + " - DNI: " + self.__dni


class Socio(Persona):
    def __init__(self, nombre, dni, numero_socio):
        super().__init__(nombre, dni)
        self.__numero_socio = numero_socio

    def get_numero_socio(self):
        return self.__numero_socio

    def mostrar_datos(self):
        return "Socio nro " + self.__numero_socio + " - " + self.get_nombre()


class Bibliotecario(Persona):
    def __init__(self, nombre, dni, usuario, clave):
        super().__init__(nombre, dni)
        self.__usuario = usuario
        self.__clave = clave

    def validar(self, usuario, clave):
        return self.__usuario == usuario and self.__clave == clave

    def mostrar_datos(self):
        return "Bibliotecario: " + self.get_nombre()