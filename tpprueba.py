# Matriz de Inquilinos
matriz_inquilinos = [
    ["ID Inquilino", "Nombre", "DNI", "Email", "Teléfono"],
    [1, "Juan Pérez", "30123456", "juan@mail.com", "+54 11 4567-8901"],
    [2, "María López", "28999888", "maria@mail.com", "+54 9 351 555-1111"],
    [3, "Carlos Díaz", "31222333", "carlos@mail.com", "+54 11 4444-2222"],
    [4, "Ana Torres", "30111222", "ana@mail.com", "+54 341 555-3333"],
    [5, "Luis Gómez", "30333444", "luis@mail.com", "+54 261 444-5555"]
]

# Matriz de Propiedades
matriz_propiedades = [
    ["ID Propiedad", "Dirección", "Tipo", "Precio Alquiler", "Estado"],
    [101, "Av. Siempre Viva 742", "Departamento", 75000, "Libre"],
    [102, "Calle Falsa 123", "Casa", 95000, "Ocupada"],
    [103, "Belgrano 456", "Departamento", 80000, "Libre"],
    [104, "San Martín 321", "Local", 120000, "Ocupada"],
    [105, "Mitre 555", "Casa", 98000, "Libre"]
]

# Matriz de Contratos
matriz_contratos = [
    ["ID Contrato", "ID Propiedad", "ID Inquilino", "Fecha Inicio", "Fecha Fin"],
    [5001, 101, 1, "2025-03-01", "2026-02-28"],
    [5002, 102, 2, "2024-05-15", "2025-05-14"],
    [5003, 103, 3, "2025-01-10", "2026-01-09"],
    [5004, 104, 4, "2025-07-01", "2026-06-30"],
    [5005, 105, 5, "2024-11-20", "2025-11-19"]
]

# Matriz de Pagos
matriz_pagos = [
    ["ID Pago", "ID Contrato", "Fecha Pago", "Monto", "Método"],
    [9001, 5001, "2025-04-01", 75000, "Transferencia"],
    [9002, 5002, "2024-06-01", 95000, "Efectivo"],
    [9003, 5003, "2025-02-01", 80000, "Transferencia"],
    [9004, 5004, "2025-08-01", 120000, "Tarjeta"],
    [9005, 5005, "2024-12-01", 98000, "Transferencia"]
]
