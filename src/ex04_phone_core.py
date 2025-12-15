"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str: 
    s = s.strip()
    parts = s.split("-")
    if len(parts) != 3:
        raise ValueError("debe haber exactamente 3 partes separadas por '-'")
    if not parts[0].startswith("+"):
        raise ValueError("la primera parte debe comenzar por '+'")
    if not parts[1].isdigit():
        raise ValueError("la parte central debe ser numerica")
    return parts[1]

    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    raise NotImplementedError("Implementa phone_core(s)")