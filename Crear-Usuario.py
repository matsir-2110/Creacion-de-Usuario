#Programa para Crear Usuario con restricciones

#Print de condiciones
print("\t-CREAR CUENTA-")
print("\t-El nombre de usuario debe tener de 5 a 15 caracteres-")
print("\t-La contraseña debe tener al menos 8 caracteres, incluyendo una mayúscula, una minúscula y un número.\n")

#Creación de usuario
while True:
    usuario = input("Nombre de Usuario (5-15 caracteres): ")

    #Condición para q deje de pedir el nombre
    if len(usuario) >= 5 and len(usuario) <= 15:
        break
    else:
        print("NO CUMPLISTE CON LAS CONDICIONES DEL NOMBRE. VOLVE A INTENTAR")

#Creación de contraseña
cont_may = False
cont_min = False
cont_num = False
caracter = 0
while True:
    contrasena = input("Contraseña: ")
    for caracter in contrasena:
        #Pregunta si "caracter" es mayuscula en esa iteracion de "contrasena" 
        if caracter.isupper():
            cont_may = True
        #Pregunta si "caracter" es minuscula en esa iteracion de "contrasena" 
        if caracter.islower():
            cont_min = True
        #Pregunta si "caracter" es un numero en esa iteracion de "contrasena" 
        if caracter.isdigit():
            cont_num = True

    #Condición para q deje de pedir la contraseña
    if cont_min == True and cont_may == True and cont_num  == True and len(contrasena) >= 8:
        break
    else:
        print("NO CUMPLISTE CON LAS CONDICIONES DE LA CONTRASEÑA. VOLVE A INTENTAR")
