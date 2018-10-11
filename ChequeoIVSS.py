# AUTORES:
#   Francisco Marcos    11-10569
#   Julio Perez         14-10820

from datetime import datetime, date

# Calcula la edad de una persona a partit de su fecha de nacimiento.
def calculador_de_edad(nacimiento):
    today = date.today()
    return today.year - nacimiento.year - (((today.month, today.day) < (nacimiento.month, nacimiento.day)))

# Verifica el genero de una persona, para el valor de masculino devulve ´verdadero´ y ´falso´ para femenino.
def chequeo_de_genero(letra_de_genero):
    return letra_de_genero == "M" or letra_de_genero == "m"

# Verifica que la cantidad de horas cotizadas sea mayor o igual a 750 horas, de lo contrario retorna falso
def chequeo_de_semanas(weeks):
    return weeks >= 750

# Calcula la cantidad de anos que se decuentas por trabajos realizados en condiciones isalubres
def descuento(anos_insalubres):
    return min(anos_insalubres // 4, 5)
    
# funcion principal que recibe como parametro edad, genero, semanas cotizadas y anos que trabajo en condiciones insalubres
def chequeo_IVSS(fecha, genero, semanas, anos_insalubres):
    fecha =  datetime.strptime(fecha, "%d %m %Y")
    age = calculador_de_edad(fecha)
    semanas = int(semanas)
    anos_insalubres = int(anos_insalubres)
    genero = chequeo_de_genero(genero)
    if (genero and age >= (60 - descuento(anos_insalubres))) or (not(genero) and age >= (55 - descuento(anos_insalubres))):
        return chequeo_de_semanas(semanas)
    else:
        return False 
