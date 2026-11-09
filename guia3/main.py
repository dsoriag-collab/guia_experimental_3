from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from utils import leer_entero
from utils import leer_texto
from utils import leer_fecha
from utils import menu
from utils import borrar_pantalla
from utils import pausar

pila = MiPila(10)
cola = MiCola(10)

# Funciones de apoyo mi_cola


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A"),
    ]


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ", 1)
    nombre = leer_texto("  Nombre: ")
    cedula = leer_texto("  Cédula: ")
    edad = leer_entero("  Edad: ")
    fecha = leer_fecha()
    destino = leer_texto("  Destino: ")
    asiento = leer_texto("  Asiento: ").upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


# pas1 = Pasajero(12, "Ana", "34443", 34, date(), "Cuenca", "12A")

# pas = leer_pasajero()
# print(pas)


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        borrar_pantalla()
        op = menu(
            "Menú Pila",
            [
                "1) Entrar a la pila",
                "2) listar",
                "3) desapilar",
                "4) Ver tope",
                "5) Buscar por número",
                "6) Modificar destino y asiento",
                "7) Eliminar por número",
                "8) Copiar",
                "9) Longitud / ¿vacía?",
                "C) Cargar datos de prueba",
                "0) Salir",
            ],
        )

        if op == "1":  # ✅ ejemplo resuelto
            borrar_pantalla()
            pasajero = leer_pasajero()  # 1. LEER
            if pila.apilar(pasajero):  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope")  # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero is None:
                print("Pila vacía")
            else:
                print("Salió:", pasajero)
                nuevo = pila.ver_tope()
                if nuevo is None:
                    print("Pila vacía")
                else:
                    print("Nuevo tope:", nuevo)
        elif op == "4":
            pasajero = pila.ver_tope()
            if pasajero is None:
                print("Pila vacía")
            else:
                print("Tope:", pasajero)
        elif op == "5":
            numero = leer_entero("Número de pasajero: ", 1)
            pos = pila.buscar(numero)
            if pos == -1:
                print("No existe")
            else:
                print(f"Encontrado en [{pos}]: {pila.datos[pos]}")
        elif op == "6":
            numero = leer_entero("Número de pasajero: ", 1)
            destino = leer_texto("Nuevo destino: ")
            asiento = leer_texto("Nuevo asiento: ").upper()
            if pila.modificar(numero, destino, asiento):
                print("Pasajero modificado")
        elif op == "7":
            numero = leer_entero("Número de pasajero: ", 1)
            if pila.eliminar_por_numero(numero):
                print("Pasajero eliminado")
        elif op == "8":
            copia = pila.copiar()
            print("Copia de la pila")
            copia.listar()
        elif op == "9":
            print("Longitud:", pila.longitud())
            print("Está vacía:", pila.esta_vacia())
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")
        elif op == "0":
            print("Hasta pronto!!!")
            break
        else:
            print("  Opción no válida")

        pausar()  # PAUSA ANTES DE VOLVER AL MENÚ


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        borrar_pantalla()
        op = menu(
            "Menú Cola",
            [
                "1) Entrar a la cola",
                "2) listar",
                "3) desencolar",
                "4) Ver frente",
                "5) Buscar por número",
                "6) Modificar destino y asiento",
                "7) Eliminar por número",
                "8) Copiar",
                "9) Longitud / ¿vacía?",
                "10) Ordenar por número",
                "11) Búsqueda binaria por número",
                "C) Cargar datos de prueba",
                "0) Salir",
            ],
        )

        if op == "1":  # ✅ ejemplo resuelto
            borrar_pantalla()
            pasajero = leer_pasajero()  # 1. LEER
            if cola.encolar(pasajero):  # 2. LLAMAR
                print("  ✓ Encolado: está al final")  # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero is None:
                print("Cola vacía")
            else:
                print("Salió:", pasajero)
                nuevo = cola.ver_frente()
                if nuevo is None:
                    print("Cola vacía")
                else:
                    print("Nuevo frente:", nuevo)
        elif op == "4":
            pasajero = cola.ver_frente()
            if pasajero is None:
                print("Cola vacía")
            else:
                print("Frente:", pasajero)
        elif op == "5":
            numero = leer_entero("Número de pasajero: ", 1)
            pos = cola.buscar(numero)
            if pos == -1:
                print("No existe")
            else:
                print(f"Encontrado en [{pos}]: {cola.datos[pos]}")
        elif op == "6":
            numero = leer_entero("Número de pasajero: ", 1)
            destino = leer_texto("Nuevo destino: ")
            asiento = leer_texto("Nuevo asiento: ").upper()
            if cola.modificar(numero, destino, asiento):
                print("Pasajero modificado")
        elif op == "7":
            numero = leer_entero("Número de pasajero: ", 1)
            if cola.eliminar_por_numero(numero):
                print("Pasajero eliminado")
        elif op == "8":
            copia = cola.copiar()
            print("Copia de la cola")
            copia.listar()
        elif op == "9":
            print("Longitud:", cola.longitud())
            print("Está vacía:", cola.esta_vacia())
        elif op == "10":
            cola.ordenar()
            print("Cola ordenada por número de pasajero")
            cola.listar()
        elif op == "11":
            numero = leer_entero("Número de pasajero: ", 1)
            pos = cola.busqueda_binaria(numero)
            if pos is None:
                print("Primero ordene la cola con la opción 10")
            elif pos == -1:
                print("No existe")
            else:
                print(f"Encontrado en [{pos}]: {cola.datos[pos]}")
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")
        elif op == "0":
            print("Hasta pronto!!!")
            break
        else:
            print("  Opción no válida")

        pausar()  # PAUSA ANTES DE VOLVER AL MENÚ


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        borrar_pantalla()
        op = menu("Menú principal", ["1) Pila", "2) Cola", "0) Salir"])

        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
