import re
from datetime import datetime

def norm(s: str) -> str:
    """Quita espacios extremos."""
    return s.strip()

def nonempty(s: str) -> bool:
    """True si no está vacío (ignorando espacios)."""
    return bool(s.strip())

def parse_int(s: str):
    """Devuelve int o None (más robusto que isdigit)."""
    try:
        return int(s.strip())
    except (TypeError, ValueError):
        return None

def pwd_ok(s: str) -> bool:
    """Valida que la contraseña tenga al menos 4 caracteres."""
    return len(s) >= 4

def parse_float(s: str):
    """Devuelve float o None."""
    try:
        return float(s.strip())
    except (TypeError, ValueError):
        return None

def parse_date(s: str):
    """
    Valida formato de fecha AAAA-MM-DD usando datetime.
    Devuelve la fecha como string si es válida, o None si no lo es.
    """
    try:
        fecha = datetime.strptime(s.strip(), '%Y-%m-%d')
        return fecha.strftime('%Y-%m-%d')
    except ValueError:
        return None

def validar_fecha(s: str) -> bool:
    """
    Valida que la fecha tenga formato AAAA-MM-DD y sea una fecha válida.
    Retorna True si es válida, False en caso contrario.
    """
    return parse_date(s) is not None

def validar_email(email: str) -> bool:
    """
    Valida que el email tenga un formato correcto usando regex.
    Retorna True si es válido, False en caso contrario.
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email.strip()))
