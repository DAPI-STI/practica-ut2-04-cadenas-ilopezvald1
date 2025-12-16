"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    parts = date_str.split("/")
    if len(parts) != 3:
        raise ValueError(f"formato invalido{date_str}")
    try:
        dia = int(parts[0])
        mes = int(parts[1])
        año = int(parts[2])
    except ValueError:
        raise ValueError(f"no valido{date_str}")
    if dia < 1 or dia > 31:
        raise ValueError(f"no valido{date_str}")
    if mes < 1 or mes > 12:
        raise ValueError(f"no valido{date_str}")
    if año <= 0:
        raise ValueError(f"no valiso{date_str}")
    return(dia, mes, año)

    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    raise NotImplementedError("Implementa parse_date(date_str)")