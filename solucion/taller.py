class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre


class Vehiculo:
    def __init__(self, patente):
        self.patente = patente


class ItemDeTrabajo:
    def __init__(self, tipo, costo):
        self.tipo = tipo
        self.costo = costo
        self.orden = None


class OrdenDeTrabajo:
    def __init__(self, numero, vehiculo):
        self.numero = numero
        self.vehiculo = vehiculo
        self._items = []

    def agregar_item(self, item):
        if item.orden is not None:
            raise ValueError("el ítem ya pertenece a otra orden de trabajo")
        item.orden = self
        self._items.append(item)

    def items(self):
        return tuple(self._items)

    def presupuesto(self):
        return sum(item.costo for item in self._items)


class Taller:
    def __init__(self):
        self._lista_mecanicos = set()

    def agregar_mecanico(self, mecanico):
        self._lista_mecanicos.add(mecanico)

    def mecanicos(self):
        return frozenset(self._lista_mecanicos)