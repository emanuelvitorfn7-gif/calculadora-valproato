# Calculadora de Valproato (Depakene)
# Cada caixa tem 50 comprimidos e nao pode fracionar.

import math

COMPRIMIDOS_POR_CAIXA = 50


def calcular_mensal(mg, meses, cp_por_mes, sobra_inicial=0):
    # validacao simples
    if mg not in (250, 500):
        raise ValueError("Miligramagem tem que ser 250 ou 500.")
    if meses <= 0:
        raise ValueError("Meses tem que ser maior que zero.")
    if cp_por_mes <= 0:
        raise ValueError("Comprimidos por mes tem que ser maior que zero.")
    if sobra_inicial < 0:
        raise ValueError("Sobra inicial nao pode ser negativa.")

    linhas = []
    sobra = sobra_inicial
    total_caixas = 0

    for mes in range(1, meses + 1):
        falta = cp_por_mes - sobra
        if falta < 0:
            falta = 0

        if falta == 0:
            caixas = 0
        else:
            caixas = math.ceil(falta / COMPRIMIDOS_POR_CAIXA)

        recebe = caixas * COMPRIMIDOS_POR_CAIXA
        sobra_final = sobra + recebe - cp_por_mes

        linhas.append({
            "mes": mes,
            "caixas": caixas,
            "sobra_final": sobra_final,
        })

        sobra = sobra_final
        total_caixas = total_caixas + caixas

    return {
        "mg": mg,
        "meses": meses,
        "linhas": linhas,
        "total_caixas": total_caixas,
        "sobra_final": sobra,
    }
