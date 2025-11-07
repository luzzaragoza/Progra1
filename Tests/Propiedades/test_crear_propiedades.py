import json
import builtins
import os
from Propiedades import crear

def test_crear_propiedad_basico(monkeypatch, tmp_path):
    # 1️⃣ Preparamos un archivo temporal para datos.json
    ruta_propiedades = tmp_path / "datos.json"
    with ruta_propiedades.open("w", encoding="utf-8") as f:
        json.dump({}, f)

    # 2️⃣ Reemplazamos la ruta del archivo original por la temporal
    monkeypatch.setattr(crear, "cargar_propiedades", lambda: {})
    monkeypatch.setattr(crear, "guardar_propiedades", lambda props: props)

    # 3️⃣ Simulamos las respuestas del usuario (input)
    respuestas = iter([
        "Belgrano 456",  # dirección
        "2",             # tipo
        "80000"          # precio
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(respuestas))

    # 4️⃣ Simulamos tipo_propiedad (para no depender del otro módulo)
    monkeypatch.setattr(crear, "tipo_propiedad", lambda op: "Departamento")

    # 5️⃣ Ejecutamos la función
    resultado = crear.crear_propiedad(103)

    # 6️⃣ Verificamos que se haya creado correctamente
    assert 103 in resultado
    prop = resultado[103]
    assert prop["Direccion"] == "Belgrano 456"
    assert prop["Tipo"] == "Departamento"
    assert prop["PrecioAlquiler"] == 80000
    assert prop["Estado"] == "Disponible"
