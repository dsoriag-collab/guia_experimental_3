import os
from datetime import date


def borrar_pantalla():
    os.system("cls") if os.name == "nt" else "clear"


def leer_entero(mensaje, minimo=0):
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= minimo:
                return numero
            print(f"Ingrese un número desde {minimo}.")
        except ValueError:
            print("  Debe ser un número entero.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Ingrese un dato.")


def leer_fecha():
    while True:
        fecha = input("Fecha de vuelo (AAAA-MM-DD): ").strip()
        try:
            if date.fromisoformat(fecha).isoformat() == fecha:
                return fecha
        except ValueError:
            pass
        print("Ingrese una fecha válida con el formato AAAA-MM-DD.")


def menu(titulo, opciones):
    print(f"\n------- {titulo} --------")
    for opcion in opciones:
        print(f" {opcion}")

    return input("Opción: ").strip().upper()


if __name__ == "__main__":
    opc = menu("Menú principal", ["1) Pila", "2) Cola", "0) Salir"])

    opc1 = menu(
        "Menú Pila",
        [
            "1) Entrar a la pila",
            "2) listar",
            "3) desapilar",
            "4) Cargar datos de prueba",
            "0) Salir",
        ],
    )

    opc2 = menu(
        "Menú Cola",
        [
            "1) Entrar a la cola",
            "2) listar",
            "3) desencolar",
            "4) Cargar datos de prueba",
            "0) Salir",
        ],
    )


def pausar():
    input("\nPresiona ENTER para continuar...")
