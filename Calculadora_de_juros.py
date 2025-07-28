def juros_simples1 ():
    while True:
        try:
            c = float(input("Digite o capital inicial: "))
            break
        except ValueError:
            print ("Insira apenas números!")
    while True:
            try:
                i = float(input("Digite a taxa de juros (em %): "))/100
                break
            except ValueError:
                print  ("Insira apenas números.")
    while True:
            try:
                t = int(input("Digite o tempo (em meses): "))
                break
            except ValueError: 
                 print ("Digite apens números")

    juros = c * i * t
    print(f"O valor do juros simples é: {juros}")

juros_simples1()

        
def var_just_number(text):
    while True:
        try:
            t = int(input(text))

        except ValueError: 
                print ("Digite apens números")
        return t
    


def juros_simples ():
    c = var_just_number("Digite o capital inicial: ")
    i= var_just_number(float("Digite a taxa de juros (em %): "))/100
    t=var_just_number(("Digite o tempo (em meses): "))

    juros = c * i * t
    print(f"O valor do juros simples é: {juros}")


juros_simples()