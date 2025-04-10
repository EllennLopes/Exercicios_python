def quadrado(lado):
    area_quadrado = (lado**2)
    return area_quadrado

def retângulo (base, altura):
    area_retangulo = base * altura 
    return area_retangulo

def triângulo (base, altura):
    area_triangulo = base * altura/2
    return area_triangulo

def círculo (pi,raio):
    area_circulo = pi * (raio **2)
    return area_circulo

def main ():
    while True:
        escolha = input("Qual área você quer calcular? Insira Q para quadrado, T para triângulo, R para retângulo ou C para círculo (q/r/t/c): ").strip()
        if escolha == 'q':
            lado= float(input("digite o lado do quadrado em cm: "))
            area  = quadrado (lado)
            print(f"a área do quadrado é {area} cm2")
        elif escolha == 'r':
            base = float(input("digite o valor da base em cm "))
            altura = float(input("digite a altura em cm "))
            area = retângulo (base, altura)
            print (f"a área do retângulo é {area} cm2")
        elif escolha == 't':
            base = float(input("digite o valor da base em cm: "))
            altura = float(input("digite o valor da altura em cm: "))
            area = triângulo (base, altura)
            print (f"a área do triângulo em cm é {area} cm2")
        elif escolha == 'c': 
            pi = 3.14
            raio = float(input("digite o valor do raio em cm: "))
            area = círculo (pi, raio)
            print (f"a área do círculo em cm é {area}")
        else: 
            print ("Escolha inválida, por favor selecione uma opção válida")
        
        continuar = input("Quer fazer outro cálculo? (sim/não): ")
        if continuar != 'sim':
            break

main()


        



    
        
