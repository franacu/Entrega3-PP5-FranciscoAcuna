import pytest
from solucion.estacionamiento import (
    Estadia, EstadiaMensual, Nocturna, FinDeSemana,
    ModificadorTarifa, facturar,
)


def test_calculo_con_modificador():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(Nocturna())
    assert estadia.total(1000) == 2400


def test_validacion_horas_negativas():
    with pytest.raises(ValueError):
        Estadia("AB123CD", -1)


def test_rechaza_modificador_invalido():
    estadia = Estadia("AB123CD", 2)
    with pytest.raises(TypeError):
        estadia.agregar_modificador("no soy un modificador")


def test_modificadores_es_inmutable_desde_afuera():
    estadia = Estadia("AB123CD", 2)
    estadia.agregar_modificador(Nocturna())

    tupla_externa = estadia.modificadores
    tupla_externa = tupla_externa + (FinDeSemana(),)  # esto crea una tupla NUEVA

    # el estado interno no debería haberse alterado
    assert estadia.total(1000) == 2400


def test_estadia_mensual_propaga_validacion_de_horas():
    with pytest.raises(ValueError):
        EstadiaMensual("XY987ZW", -1, descuento=20)


def test_estadia_mensual_con_descuento():
    mensual = EstadiaMensual("XY987ZW", 2, descuento=20)
    mensual.agregar_modificador(Nocturna())
    assert mensual.total(1000) == 1920


def test_facturar_lista_mixta():
    e1 = Estadia("AB123CD", 2)
    e1.agregar_modificador(Nocturna())

    e2 = EstadiaMensual("XY987ZW", 2, descuento=20)
    e2.agregar_modificador(Nocturna())

    total = facturar([e1, e2], tarifa_por_hora=1000)
    assert total == 2400 + 1920