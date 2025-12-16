"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    standard_price = price_str.replace(',', '.')
    parts = standard_price.split('.')
    if len(parts) == 1:
        raise ValueError(f"faltan los decimales. recibido: {price_str}")
    elif len(parts) != 2:
        raise ValueError(f"separadores decimales{price_str}")
    euros_str, cents_str = parts
    if len(cents_str) != 2:
        raise ValueError(f"los centimos tienen que tener dos decimales{price_str}")
    try:
        euros = int(euros_str)
        centimos = int(cents_str)
    except ValueError:
        raise ValueError(f"faltan los separadores{price_str}")
    return (euros, centimos)
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    raise NotImplementedError("Implementa euros_cents(price_str)")