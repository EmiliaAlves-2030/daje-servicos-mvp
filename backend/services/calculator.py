def calcular_insumos(area_m2: float, margem_perda: float = 0.10):
    if area_m2 <= 0:
        raise ValueError("A área deve ser maior que zero.")
    
    area_total = area_m2 * (1 + margem_perda)
    argamassa_kg = area_total * 4.5
    
    return {
        "area_liquida_m2": round(area_m2, 2),
        "area_com_margem_m2": round(area_total, 2),
        "argamassa_kg": round(argamassa_kg, 2)
    }
