# estatistica.py
import math

def calcular_media(dados):
    """Calcula a média aritmética simples dos dados."""
    if not dados:
        return 0
    return sum(dados) / len(dados)

def calcular_mediana(dados):
    """Calcula a mediana (ponto central) dos dados."""
    if not dados:
        return 0
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    meio = n // 2
    if n % 2 == 0:
        return (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
    return dados_ordenados[meio]

def calcular_desvio_padrao(dados):
    """Calcula o desvio padrão populacional dos dados."""
    if not dados:
        return 0
    media = calcular_media(dados)
    variancia = sum((x - media) ** 2 for x in dados) / len(dados)
    return math.sqrt(variancia)
