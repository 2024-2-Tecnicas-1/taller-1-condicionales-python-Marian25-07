def evaluar(num_victorias_a, num_victorias_b):
    # Evaluar si A o B ganó, si aún no termina o si es inválido
    if (num_victorias_a >= 6 and num_victorias_a - num_victorias_b >= 2) or (num_victorias_a == 7 and num_victorias_b == 5 or num_victorias_b == 6):
        return "Ganó A"
    elif (num_victorias_b >= 6 and num_victorias_b - num_victorias_a >= 2) or (num_victorias_b == 7 and num_victorias_a == 5 or num_victorias_a == 6):
        return "Ganó B"
    elif num_victorias_a > 7 or num_victorias_b > 7:
        return "Inválido"
    else:
        return "Aún no termina"

if __name__ == '__main__':
    print("Los juegos ganados por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganados por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta) 
