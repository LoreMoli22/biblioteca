from modelos.persona import Socio, Bibliotecario
from modelos.libro import Libro
from modelos.biblioteca import Biblioteca


def cargar_datos(biblioteca):
    biblioteca.agregar_libro(Libro("El Principito", "Saint-Exupery", "111"))
    biblioteca.agregar_libro(Libro("Rayuela", "Cortazar", "222"))
    biblioteca.agregar_libro(Libro("Ficciones", "Borges", "333"))
    biblioteca.agregar_socio(Socio("Ana", "123", "1"))
    biblioteca.agregar_socio(Socio("Juan", "456", "2"))


def iniciar_sesion(bibliotecario):
    print("=== BIBLIOTECA ===")
    while True:
        usuario = input("Usuario: ")
        clave = input("Clave: ")
        if bibliotecario.validar(usuario, clave):
            print("Bienvenida, " + bibliotecario.get_nombre())
            return
        print("Datos incorrectos")


def registrar_libro(biblioteca):
    print("=== REGISTRAR LIBRO ===")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    codigo = input("Codigo: ")
    if biblioteca.agregar_libro(Libro(titulo, autor, codigo)):
        print("Libro registrado")
    else:
        print("Ya existe un libro con ese codigo")


def registrar_socio(biblioteca):
    print("=== REGISTRAR SOCIO ===")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    numero = input("Nro de socio: ")
    if biblioteca.agregar_socio(Socio(nombre, dni, numero)):
        print("Socio registrado")
    else:
        print("Ya existe un socio con ese numero")


def prestar_libro(biblioteca):
    print("=== PRESTAR LIBRO ===")
    numero = input("Nro de socio: ")
    codigo = input("Codigo: ")
    print(biblioteca.prestar(numero, codigo))


def devolver_libro(biblioteca):
    print("=== DEVOLVER LIBRO ===")
    codigo = input("Codigo: ")
    print(biblioteca.devolver(codigo))


def buscar_libro(biblioteca):
    print("=== BUSCAR LIBRO ===")
    texto = input("Titulo a buscar: ")
    resultado = biblioteca.buscar_por_titulo(texto)
    if len(resultado) == 0:
        print("No se encontraron libros")
    for libro in resultado:
        print(libro.mostrar_datos())


def ver_prestamos(biblioteca):
    print("=== PRESTAMOS ACTIVOS ===")
    activos = biblioteca.get_prestamos_activos()
    if len(activos) == 0:
        print("No hay prestamos activos")
    for prestamo in activos:
        print(prestamo.mostrar_datos())


def main():
    biblioteca = Biblioteca("Biblioteca Popular")
    bibliotecario = Bibliotecario("Marta", "789", "admin", "1234")
    cargar_datos(biblioteca)
    iniciar_sesion(bibliotecario)

    opcion = ""
    while opcion != "0":
        print("")
        print("=== MENU PRINCIPAL ===")
        print("1. Registrar libro")
        print("2. Registrar socio")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro")
        print("6. Ver prestamos")
        print("0. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            registrar_socio(biblioteca)
        elif opcion == "3":
            prestar_libro(biblioteca)
        elif opcion == "4":
            devolver_libro(biblioteca)
        elif opcion == "5":
            buscar_libro(biblioteca)
        elif opcion == "6":
            ver_prestamos(biblioteca)
        elif opcion == "0":
            print("Hasta luego")
        else:
            print("Opcion invalida")


main()