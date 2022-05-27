

def calcularIMC(peso, alturaEnMe):
    imc = peso / (alturaEnMe * alturaEnMe)
    return imc

def pedirElIMC():
    peso = float(input("Ingrese su peso en kg > "))
    alturaEnCm = float(input("Ingrese su altura en centimetros > "))


    alturaEnMe = alturaEnCm / 100
    imc = calcularIMC(peso, alturaEnMe)


    print("Su indice de masa corporal es: " + str(imc))


    if  imc < 20:
        print("Estado de delgadez")

    if  imc >= 20 and imc < 26:
        print("Peso normal")

    if  imc >= 26 and imc <30:
        print("Estado de sobrepeso")        

    if imc >= 30:
        print("Estado de obesidad")

pedirElIMC()