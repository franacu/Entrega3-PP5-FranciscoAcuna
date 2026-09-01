# Taller mecánico

## Análisis

Conceptos: orden de trabajo, ítem de trabajo, vehículo, mecánico, taller.
"Presupuesto" no es clase: se calcula sumando costos, no tiene estado propio.

## Tarjetas CRC

Mecanico: sabe su nombre.
Vehiculo: sabe su patente.
ItemDeTrabajo: sabe tipo, costo y a qué orden pertenece. Colaborador: OrdenDeTrabajo.
OrdenDeTrabajo: agrega items (rechaza los que ya tienen dueño), calcula presupuesto. Colaboradores: ItemDeTrabajo, Vehiculo.
Taller: agrega mecánicos a la plantilla. Colaborador: Mecanico.

## Relaciones

Taller - Mecanico: Agregación. Un mecánico existe con su propio nombre
aunque el taller no exista. No es composición porque no depende del taller
para existir.

OrdenDeTrabajo - Vehiculo: Asociación. La orden guarda una referencia al
vehículo, pero el vehículo existe independiente y puede tener otras órdenes.

ItemDeTrabajo - OrdenDeTrabajo: Composición. Un item no tiene sentido
fuera de la orden. No puede pertenecer a dos órdenes a la vez (raise en
agregar_item). No es agregación porque no se puede mover libremente a otra
orden.