from datetime import date

def evaluar(dia, mes, anno):
    # Obtener la fecha actual
    hoy = date.today()
    
    # Calcular la edad preliminar
    edad = hoy.year - anno
    
    # Ajustar la edad si aún no ha cumplido años este año
    if (hoy.month < mes) or (hoy.month == mes and hoy.day < dia):
        edad -= 1
    
    return f"Usted tiene {edad} años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)

