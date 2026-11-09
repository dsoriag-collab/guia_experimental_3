from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):  # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(pasajero.numero, "ya existe")
            return False
        self.datos[self.cantidad] = pasajero  # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):  # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):  # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.cantidad == 0:
            return None
        pasajero = self.datos[0]
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            print(numero, "no existe")
            return False
        if not nuevo_destino.strip() or not nuevo_asiento.strip():
            print("Destino o asiento no válidos")
            return False
        self.datos[pos].destino = nuevo_destino.strip()
        self.datos[pos].asiento = nuevo_asiento.strip().upper()
        return True

    def eliminar_por_numero(self, numero):
        cantidad = self.cantidad
        eliminado = False
        for i in range(cantidad):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                eliminado = True
            else:
                self.encolar(pasajero)
        if not eliminado:
            print(numero, "no existe")
        return eliminado

    def copiar(self):
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0

    def busqueda_binaria(self, numero):
        # Para buscar por mitades, los números deben estar ordenados.
        for i in range(self.cantidad - 1):
            if self.datos[i].numero > self.datos[i + 1].numero:
                return None  # La cola aún no está ordenada.

        izquierda = 0
        derecha = self.cantidad - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            actual = self.datos[medio].numero
            if actual == numero:
                return medio
            if numero < actual:
                derecha = medio - 1
            else:
                izquierda = medio + 1
        return -1

    def ordenar(self):
        # Burbuja manual: ordena por número de pasajero (menor a mayor).
        for vuelta in range(self.cantidad - 1):
            for i in range(self.cantidad - 1 - vuelta):
                if self.datos[i].numero > self.datos[i + 1].numero:
                    auxiliar = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = auxiliar
        return True
