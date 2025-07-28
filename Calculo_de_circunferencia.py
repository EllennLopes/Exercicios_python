<<<<<<< HEAD
def pi():
    return 3.14159 

def altura():
    altura_valor = float(input("altura em cm:"))
    return altura_valor
def raio():
    raio_valor = float(input ("raio em cm: ")) 
    return raio_valor

def volume_circunferencia():
    r = raio()
    h = altura()
    volume = pi() * (r**2) * h 
    print (f" O volume da circunferência é {round(volume,2)} cm3")

=======
def pi():
    return 3.14159 

def altura():
    altura_valor = float(input("altura em cm:"))
    return altura_valor
def raio():
    raio_valor = float(input ("raio em cm: ")) 
    return raio_valor

def volume_circunferencia():
    r = raio()
    h = altura()
    volume = pi() * (r**2) * h 
    print (f" O volume da circunferência é {round(volume,2)} cm3")

>>>>>>> a5049ff4e84c593fc76a202aeff86fa1dace9175
volume_circunferencia()