from abc import ABC, abstractmethod


class ModificadorTarifa(ABC):
    @abstractmethod
    def aplicar(self, total: float, horas: int) -> float:
        """Devuelve el nuevo total."""


class Estadia:
    def __init__(self, patente, horas):
        self.patenteIng = self._validarPatente(patente)
        self.horasIng = self._validarHoras(horas)
        self._modificadores = []

    @staticmethod
    def _validarHoras(horas):
        if horas <= 0:
            raise ValueError("No existe horas en negativo")
        return horas

    @staticmethod
    def _validarPatente(patente):
        if not patente or patente.strip() == "":
            raise ValueError("Campo Vacio")
        return patente

    def agregar_modificador(self, modificador):
        if not isinstance(modificador, ModificadorTarifa):
            raise TypeError("El modificador no cumple el contrato")
        self._modificadores.append(modificador)

    @property
    def modificadores(self):
        return tuple(self._modificadores)

    def total(self, tarifa_por_hora):
        if tarifa_por_hora <= 0:
            raise ValueError("La tarifa por hora debe ser mayor que cero")

        total = self.horasIng * tarifa_por_hora
        for modificador in self.modificadores:
            total = modificador.aplicar(total, self.horasIng)
        return total


class EstadiaMensual(Estadia):
    def __init__(self, patente, horas, descuento):
        super().__init__(patente, horas)
        if descuento < 0 or descuento > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")
        self.descuento = descuento

    def total(self, tarifa_por_hora):
        total = super().total(tarifa_por_hora)
        return total * (1 - self.descuento / 100)


def facturar(estadias, tarifa_por_hora):
    return sum(estadia.total(tarifa_por_hora) for estadia in estadias)


class Nocturna(ModificadorTarifa):
    """Agrega $200 por cada hora de estadía."""
    def aplicar(self, total, horas):
        return total + 200 * horas


class FinDeSemana(ModificadorTarifa):
    """Multiplica el total acumulado hasta el momento por 1.5."""
    def aplicar(self, total, horas):
        return total * 1.5