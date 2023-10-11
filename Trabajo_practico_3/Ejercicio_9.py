password = "Contraseña1"

while(True):
    try_password = input("Ingrese su contraseña: ")
    if(try_password == password):
        break;
    else:
        print("Contraseña incorrecta")
        print()

print("Acceso exitoso")