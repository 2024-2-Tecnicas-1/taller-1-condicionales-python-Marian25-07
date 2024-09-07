def evaluar(dividendo, divisor):
    # Calcula el cociente y el residuo
    cociente = dividendo // divisor  # División entera
    residuo = dividendo % divisor  # Residuo de la división

    if residuo == 0:
        respuesta = f"La división es exacta.\nCociente: {cociente}\nResiduo: {residuo}"
    else:
        respuesta = f"La división no es exacta.\nCociente: {cociente}\nResiduo: {residuo}"

    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)

