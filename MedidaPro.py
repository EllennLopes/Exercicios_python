def calcular_materiais_revestimento(largura, comprimento, tamanho_peca_m2, margem_percentual):
    area = largura * comprimento
    margem_decimal = margem_percentual / 100
    area_com_sobra = area * (1 + margem_decimal)

    quantidade_pecas = round(area_com_sobra / tamanho_peca_m2)
    argamassa_kg = round(area_com_sobra * 4)     # 4kg por m² com margem
    rejunte_kg = round(area_com_sobra * 0.5)     # 0.5kg por m² com margem

    return {
        "Área (m²)": round(area, 2),
        "Área com sobra (m²)": round(area_com_sobra, 2),
        "Quantidade de peças": quantidade_pecas,
        "Argamassa necessária (kg)": argamassa_kg,
        "Rejunte necessário (kg)": rejunte_kg
    }

def pedir_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Por favor, insira apenas números válidos.")

def exibir_resultado(resultado):
    print("\n--- Resultado ---")
    for item, valor in resultado.items():
        print(f"{item}: {valor}")

def main():
    print("📐 Calculadora de Materiais para Revestimento\n")

    largura = pedir_float("Informe a largura do ambiente (m): ")
    comprimento = pedir_float("Informe o comprimento do ambiente (m): ")
    tamanho_peca = pedir_float("Informe o tamanho da peça em m² (ex: 0.36): ")
    margem = pedir_float("Informe a margem de sobra desejada (%): ")

    resultado = calcular_materiais_revestimento(largura, comprimento, tamanho_peca, margem)
    exibir_resultado(resultado)

if __name__ == "__main__":
    main()
