# Sistema de Biblioteca

Parcial domiciliario de Algoritmos y estructuras de datos III
ISFT N° 210 – La Plata

Sistema por consola para registrar libros, socios, préstamos y devoluciones de una biblioteca, desarrollado en Python aplicando Programación Orientada a Objetos.

## Cómo ejecutarlo

Requiere Python 3 y Git. No usa librerías externas.

### En Linux o Mac

1. Clonar el repositorio:

    git clone https://github.com/LoreMoli22/biblioteca.git

2. Entrar a la carpeta:

    cd biblioteca

3. Ejecutar el programa:

    python3 main.py

### En Windows, el último paso es `python main.py`.

### Sin Git

Descargar desde el botón verde **Code** → **Download ZIP**, descomprimir, abrir una terminal dentro de la carpeta y ejecutar `python3 main.py` (Linux o Mac) o `python main.py` (Windows)

## Datos de acceso:

- Usuario: `admin`
- Clave: `1234`

Al iniciar, el sistema ya tiene cargados 3 libros (códigos 111, 222 y 333) y 2 socios (números 1 y 2) para poder probarlo.

## Estructura

```
biblioteca/
├── main.py              Menú principal
└── modelos/
    ├── persona.py       Persona, Socio, Bibliotecario
    ├── libro.py         Libro
    ├── prestamo.py      Prestamo
    └── biblioteca.py    Biblioteca
```

## Conceptos de POO aplicados

- **Encapsulamiento**: todos los atributos son privados y se acceden con métodos.
- **Herencia**: Socio y Bibliotecario heredan de Persona.
- **Polimorfismo**: cada clase redefine `mostrar_datos()`.
- **Asociación**: Prestamo vincula un Socio con un Libro.
- **Agregación**: Biblioteca contiene libros y socios creados afuera.
- **Composición**: Biblioteca crea sus préstamos, que no existen sin ella.