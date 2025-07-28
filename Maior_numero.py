<<<<<<< HEAD
def verificar_numero():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    elif numero1 < numero2:
        maior = numero2
        menor = numero1
    else:
        print("Os números são iguais")
        return
    
    print(f"O maior número é {maior} e o menor número é {menor}")

verificar_numero()    

=======
def verificar_numero():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
    
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    elif numero1 < numero2:
        maior = numero2
        menor = numero1
    else:
        print("Os números são iguais")
        return
    
    print(f"O maior número é {maior} e o menor número é {menor}")

verificar_numero()    

>>>>>>> a5049ff4e84c593fc76a202aeff86fa1dace9175
