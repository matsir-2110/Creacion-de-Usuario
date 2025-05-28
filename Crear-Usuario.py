#Programa para Crear Usuario con restricciones

#Creación de usuario
while True:
    usuario = input("Nombre de Usuario: ")

    for caracter in usuario:
        #Pregunta si "caracter" es mayuscula en esa iteracion de "usuario" 
        if caracter.isupper():
            cont_may = True
        #Pregunta si "caracter" es minuscula en esa iteracion de "usuario" 
        if caracter.islower():
            cont_min = True
        #Pregunta si "caracter" es un numero en esa iteracion de "usuario" 
        if caracter.isnumeric():
            cont_num = True

    #Condición para q deje de pedir el nombre
    if cont_min == True and cont_may == True and cont_num == True:
        break

