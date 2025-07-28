def calcular_materiais(largura, comprimento, tamanho_peca_m2, margem_percentual):
    area = largura * comprimento
    margem_decimal = margem_percentual / 100
    area_com_sobra = area * (1 + margem_decimal)
    quantidade_pecas = round(area_com_sobra / tamanho_peca_m2)
    argamassa_kg = round(area * 4)  # 4kg por m²
    rejunte_kg = round(area * 0.5)  # 0.5kg por m²
    return {
        "Área": round(area, 2),
        "Área com sobra": round(area_com_sobra, 2),
        "Quantidade de peças": quantidade_pecas,
        "Argamassa (kg)": argamassa_kg,
        "Rejunte (kg)": rejunte_kg
    }

def pedir_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira apenas números.")

def main():
    largura = pedir_float("Informe a largura do ambiente (m): ")
    comprimento = pedir_float("Informe o comprimento do ambiente (m): ")
    tamanho_peca = pedir_float("Informe o tamanho da peça em m2 (ex: 0.36): ")
    margem = pedir_float("Informe a margem de sobra desejada (%): ")

    resultado = calcular_materiais(largura, comprimento, tamanho_peca, margem)

    print("\n--- Resultado ---")
    for k, v in resultado.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()