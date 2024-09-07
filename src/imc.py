def evaluar(peso, estatura, edad):
    # Cálculo del índice de masa corporal (IMC)
    imc = peso / (estatura ** 2)
    
    # Determinar el riesgo según el valor del IMC
    if imc < 18.5:
        return "bajo"
    elif 18.5 <= imc < 25:
        return "medio"
    else:
        return "alto"

if __name__ == '__main__':
    print("Peso:", end="")
    peso = float(input())
    print("Estatura (en metros):", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(f"Su condición de riesgo es: {respuesta}")
