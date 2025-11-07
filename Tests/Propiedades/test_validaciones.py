import pytest
from FuncAux.validaciones import (
    norm, nonempty, parse_int, parse_float,
    parse_date, validar_fecha, validar_email
)

def test_norm_y_nonempty():
    assert norm("  hola  ") == "hola"
    assert nonempty("  x ") is True
    assert nonempty("   ") is False

@pytest.mark.parametrize("texto,esperado", [("10","10"), ("  -5 ","-5"), ("0","0")])
def test_parse_int_ok(texto, esperado):
    assert parse_int(texto) == int(esperado)

@pytest.mark.parametrize("texto", ["", "12.3", "abc"])
def test_parse_int_none(texto):
    assert parse_int(texto) is None

@pytest.mark.parametrize("texto,esperado", [("3.14",3.14), ("  -2 ","-2"), ("0","0")])
def test_parse_float_ok(texto, esperado):
    assert parse_float(texto) == float(esperado)

@pytest.mark.parametrize("s", ["2025-11-07", "1999-01-01", " 2024-02-29 "])
def test_parse_date_valida(s):
    out = parse_date(s)
    assert out is not None
    # siempre normalizado
    assert len(out) == 10 and out[4] == "-" and out[7] == "-"

@pytest.mark.parametrize("s", ["2025/11/07", "07-11-2025", "2025-13-01", "2025-00-10", "2025-02-30", "", " "])
def test_parse_date_invalida(s):
    assert parse_date(s) is None
    assert validar_fecha(s) is False

@pytest.mark.parametrize("mail", ["user@mail.com", "a.b+c-d@sub.dom.ar"])
def test_validar_email_ok(mail):
    assert validar_email(mail) is True

@pytest.mark.parametrize("mail", ["user@", "@dom.com", "user@dom", "user@dom.", "user dom@dom.com"])
def test_validar_email_fail(mail):
    assert validar_email(mail) is False
