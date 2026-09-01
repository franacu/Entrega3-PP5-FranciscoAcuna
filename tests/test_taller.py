import pytest
from solucion.taller import Vehiculo, ItemDeTrabajo, OrdenDeTrabajo, Mecanico, Taller


def test_presupuesto():
    v = Vehiculo("AB123CD")
    orden = OrdenDeTrabajo(1, v)

    item1 = ItemDeTrabajo("repuesto", 5000)
    item2 = ItemDeTrabajo("mano_de_obra", 3000)

    orden.agregar_item(item1)
    orden.agregar_item(item2)

    assert orden.presupuesto() == 8000


def test_item_no_puede_estar_en_dos_ordenes():
    orden1 = OrdenDeTrabajo(1, Vehiculo("AB123CD"))
    orden2 = OrdenDeTrabajo(2, Vehiculo("XY987ZW"))
    item = ItemDeTrabajo("repuesto", 5000)

    orden1.agregar_item(item)

    with pytest.raises(ValueError):
        orden2.agregar_item(item)

    assert len(orden2.items()) == 0
    assert item.orden == orden1


def test_taller_agrega_mecanico():
    taller = Taller()
    mecanico = Mecanico("Juan")

    taller.agregar_mecanico(mecanico)

    assert mecanico in taller.mecanicos()