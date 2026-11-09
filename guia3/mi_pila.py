from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):  # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print(pasajero.numero, "ya existe")
            return False
        self.datos[self.cantidad] = pasajero  # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):  # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(
            self.cantidad - 1, -1, -1
        ):  # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            return None
        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad - 1, -1, -1):
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
        aux = MiPila(self.capacidad)
        eliminado = False
        while not self.esta_vacia():
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                eliminado = True
                break
            aux.apilar(pasajero)
        while not aux.esta_vacia():
            self.apilar(aux.desapilar())
        if not eliminado:
            print(numero, "no existe")
        return eliminado

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
