
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
    """Valida formato de fecha DD-MM-AAAA y devuelve (DD, MM, AAAA) o None."""
    parts = s.strip().split("-")
    if len(parts) != 3:
        return None
    try:
        dd = int(parts[0])
        mm = int(parts[1])
        aaaa = int(parts[2])
        if not (1 <= dd <= 31 and 1 <= mm <= 12 and aaaa >= 1900):
            return None
        return (dd, mm, aaaa)
    except ValueError:
        return None