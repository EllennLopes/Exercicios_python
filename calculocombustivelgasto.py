def distancia(tempo, velocidade):
    distancia_valor = tempo * velocidade
    return distancia_valor

def obter_tempo():
    tempo_valor = float(input("tempo de viagem em horas: "))
    return tempo_valor

def obter_velocidade():    
    velocidade_valor = float(input("velocidade média em km/h: "))
    return velocidade_valor

def calcular_combustivel(distancia, consumo):
    return distancia / consumo

def combustivel_gasto():
    t = obter_tempo()
    v = obter_velocidade()
    d = distancia(t, v)
    consumo = float(input("Digite o consumo do veículo (em km por litro): "))
    combustivel = calcular_combustivel(d, consumo)
    print(f"O combustível gasto na viagem foi de {round(combustivel, 2)} litros")
