
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
