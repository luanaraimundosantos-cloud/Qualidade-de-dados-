# main.py
from estatistica import calcular_media, calcular_mediana, calcular_desvio_padrao
from simulador_gaussiana import gerar_distribuicao_gaussiana, classificar_padrao

def exibir_menu():
    print("\n==================================================")
    print("📊 CIÊNCIA DE DADOS: PREVENDO PADRÕES DE QUALIDADE DE VIDA")
    print("==================================================")
    print("1. Analisar dados de amostra manual da turma")
    print("2. Gerar e analisar Distribuição Gaussiana (Escala 100 alunos)")
    print("3. Testar Previsão de Padrão para um Aluno")
    print("4. Sair")
    print("--------------------------------------------------")

def main():
    # Amostra inicial de dados de qualidade de vida (notas de 0 a 10)
    dados_amostra = [8.5, 7.0, 9.0, 6.5, 5.0, 8.0, 7.5, 9.5, 6.0, 7.5]

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            print("\n--- Análise Estatística da Amostra Manual ---")
            print(f"Dados recolhidos: {dados_amostra}")
            media = calcular_media(dados_amostra)
            mediana = calcular_mediana(dados_amostra)
            desvio = calcular_desvio_padrao(dados_amostra)
            print(f"📌 Média: {media:.2f}")
            print(f"📌 Mediana: {mediana:.2f}")
            print(f"📌 Desvio Padrão: {desvio:.2f}")

        elif opcao == "2":
            print("\n--- Simulação em Larga Escala (Distribuição Gaussiana) ---")
            dados_larga_escala = gerar_distribuicao_gaussiana()
            media_g = calcular_media(dados_larga_escala)
            desvio_g = calcular_desvio_padrao(dados_larga_escala)
            print(f"Gerados {len(dados_larga_escala)} dados simulados com curva Gaussiana.")
            print(f"📊 Média Populacional: {media_g:.2f}")
            print(f"📊 Desvio Padrão Populacional: {desvio_g:.2f}")

        elif opcao == "3":
            print("\n--- Teste de Previsão de Padrão do Aluno ---")
            try:
                nota = float(input("Digite a pontuação do aluno (0 a 10): "))
                media_ref = calcular_media(dados_amostra)
                desvio_ref = calcular_desvio_padrao(dados_amostra)
                resultado = classificar_padrao(nota, media_ref, desvio_ref)
                print(f"\nResultado da Análise: {resultado}")
            except ValueError:
                print("⚠️ Por favor, insira um número válido.")

        elif opcao == "4":
            print("\nPrograma encerrado. Até breve!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
