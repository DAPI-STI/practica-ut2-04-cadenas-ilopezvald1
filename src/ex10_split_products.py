"""
Ejercicio 10: leer una lista de productos separados por comas y mostrar cada uno en una línea.

La función:

Recibe una cadena tipo "pan, leche, huevos".

Devuelve una lista con ["pan", "leche", "huevos"], sin espacios sobrantes.
"""

def split_products(csv_line: str) -> list[str]:
    if not csv_line:
        return []
    productos = csv_line.split(",")
    productos_limpios = [producto.strip() for producto in productos]
    productos_filtrados = [producto for producto in productos_limpios if producto]
    return productos_filtrados

    """Devuelve una lista de productos sin espacios extra a partir de una línea CSV simple."""
    # TODO: usa .split(",") y .strip() para limpiar espacios
    raise NotImplementedError("Implementa split_products(csv_line)")