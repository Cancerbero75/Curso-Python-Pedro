# CALCULAR ÁREA DE UN CUADRADO
# 1 - Solicitar la longitud del lado
# lado = float(input("Por favor, introduce la longitud de un lado del cuadrado en cm: "))

# 2 - Calcular el área
# area = lado * lado

# 3 - Mostrar el resultado
# print(f"El área del cuadrado con lado {lado} es de {area} cm.")


# CALCULAR ÁREA DE UN CUADRADO CON def
    # 1 - Solicitar la longitud del lado

# def area_cuadrado():
    
    # lado = float(input("Por favor, introduce la longitud de un lado del cuadrado en cm: "))

    # 2 - Calcular el área
    # area = lado * lado

    # 3 - Mostrar el resultado
    # print(f"El área del cuadrado con lado {lado} es de {area} cm.")

# area_cuadrado()


# CALCULAR PERÍMETRO DE UN CUADRADO
# 1 - Solicitar la longitud del lado
# lado = float(input("Por favor, introduce la longitud de un lado del cuadrado en cm: "))

# 2 - Calcular el área
# perimetro = lado + lado + lado + lado

# 3 - Mostrar el resultado
# print(f"El perimetro del cuadrado con lado {lado} es de {perimetro} cm.")


# CALCULAR PERÍMETRO DE UN CUADRADO CON def
# 1 - Solicitar la longitud del lado

# def perimetro_cuadrado():

    # lado = float(input("Por favor, introduce la longitud de un lado del cuadrado en cm: "))

# 2 - Calcular el área
    # perimetro = lado + lado + lado + lado

# 3 - Mostrar el resultado
    # print(f"El perimetro del cuadrado con lado {lado} es de {perimetro} cm.")

# perimetro_cuadrado()


# CALCULAR PERÍMETRO DE UN CUADRADO CON def y parámetro
# trabaja de manera automática sin necesidad de solicitar el calculo
# 1 - Solicitar la longitud del lado

def perimetro_cuadrado(lado):

# 1 - Calcular el área
    perimetro = lado + lado + lado + lado

# 3 - Mostrar el resultado
    print(f"El perimetro del cuadrado con lado {lado} es de {perimetro} cm.")

perimetro_cuadrado(23)
perimetro_cuadrado(25.1)
perimetro_cuadrado(63.7)

