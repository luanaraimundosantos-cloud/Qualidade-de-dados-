# simulador_gaussiana.py
import random
from estatistica import calcular_media, calcular_desvio_padrao

def gerar_distribuicao_gaussiana(media_desejada=7.5, desvio_desejado=1.2, quantidade=100):
    """Simula uma distribuição Gaussiana (Normal) de notas/pontuações de qualidade de vida."""
    random.seed(42)  # Mantém os dados consistentes para testes
    dados = [round(random.gauss(media_desejada, desvio_desejado), 2) for _ in range(quantidade)]
    # Garante que os valores fiquem no intervalo de 0 a 10
    dados = [max(0.0, min(10.0, x)) for x in dados]
    return dados

def classificar_padrao(valor, media, desvio_padrao):
    """Classifica a pontuação do aluno com base nos limites do modelo estatístico."""
    if valor >= media + desvio_padrao:
        return "Excelente (Acima do padrão da turma)"
    elif valor >= media - desvio_padrao:
        return "Dentro da Média Esperada"
    else:
        return "Abaixo da Média (Necessita de atenção)"
