# Pido al usuario que ingrese el dia de la semana en el siguiente formato dia,DD,MM
fecha = input("Ingrese el dia se la semana en el siguiente formato \"dia, DD/MM\": ").lower()
# Separo la cadena en los distintos valores que necesito comprobar
dia_semana = fecha[0:fecha.find(",")]
dia_numero = int(fecha[fecha.find(" ")+1:fecha.find("/")])
mes = int(fecha[fecha.find("/")+1:])

# Creo una lista con los dias de la semana para comprobar si el usuario ingreso un dia valido
dias_semana_lista = ["lunes","martes","miercoles","jueves","viernes"]

# Compruebo que los datos ingresados sean correctos
if dia_semana in dias_semana_lista:
    if dia_numero>0 and dia_numero<32:
        if mes>0 and mes<13:
              print("Ingreso valido")
        else: 
            ingreso_valido = False
            print("Error al ingresar datos")    
    else: 
            ingreso_valido = False
            print("Error al ingresar datos") 
else: 
            ingreso_valido = False
            print("Error al ingresar datos")                     

# Creo una lista con los dias donde se puede tomar examen
dias_examenes = dias_semana_lista[0:2]

# Compruebo que el dia elegido sea uno donde puedo tomar examen, y si es asi cargo alumnos aprobados y desaprobados
if dia_semana in dias_examenes:
      aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
      desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
      promedio_aprobados = (aprobados*100)/(aprobados+desaprobados)
      print(f"El promedio de alumnos aprobados es {promedio_aprobados}%")
# Compruebo si el dia ingresado es jueves, si es asi, compruebo si el piorcentaje de asistencia es mayor a 50%
elif dia_semana==dias_semana_lista[3]:                                             
      porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
      if porcentaje_asistencia>50:
            print("Asistio la mayoria")
      else: 
            print("No asistio la mayoria")
# Compruebo que sea viernes, dia 1 y mes 1 o 7, si es asi, ingreso cantidad de nuevos alumnos, arancel y calculo ingresos totales
elif dia_semana==dias_semana_lista[4]:
      if dia_numero==1:
            if mes==1 or mes==7:
                  print("Comienzo de nuevo ciclo")
                  nuevos_alumnos = int(input("Ingrese la cantidad de alumnos nuevos: "))
                  arancel = int(input("Ingrese el valor del arancel: "))
                  print(f"El ingreso total es {nuevos_alumnos*arancel}$") 