print("\n")

import os

#Creacion de los archivo CSV
archivos = ["doctores.csv", "pacientes.csv", "citas.csv", "horarios.csv"]

#Este bloque se hace para que python verifique que sino existe 
#el archivo nuevo (si en caso agregamso mas a la lista) lo cree al final y omitir si exite
for archivo in archivos:
    if os.path.exists(archivo):
        print("-")
    else:
        with open(archivo, "a"):
            pass

titulo = "Sistema de citas Medicas"
print(titulo)
print("-" * len(titulo))

#variable para entrar en el ciclo while
seleccion = 99

#inicio del Menú
while seleccion != 0:
    #Menú de seleccion
    seleccion = int(input("1) Registrar doctor \n"
                          "2) Registrar paciente \n"
                          "3) Registrar horarios \n"
                          "4) Agendar Cita \n"
                          "5) Consultar historial \n"
                          "6) Reportes \n"
                          "0) Salir \n"
                          "Escriba una opcion ->   "))
    
    #Lo que susede si se selecciona la opsion 1
    if seleccion == 1:

        print("\nModulo de registro de doctores\n")
        #Preguntas
        id_doctor = input("ID del doctor: ")
        nombre_doctor = input("Nombre del Doctor: ")
        especialidad = input("Especialidad del doctor: ")

        doctor_existe = False
        #Esto sirve para recorrer los datos del archivo y que python los lea en busca de coincidencias
        with open("doctores.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",") #El split se usa para separar las columnas y obtener solo el dato necesario
                if len(datos) < 3:
                    continue
                id_guardado = datos[0]
                if id_doctor == id_guardado:
                    doctor_existe = True

        if doctor_existe:
         print("El ID del doctor ya está registrado\n")

        #Aca es donde ya valido que no existe ID de doctor y permite escribir en el archivo csv
        else:
            with open("doctores.csv", "a") as archivo:
                archivo.write(f"{id_doctor},{nombre_doctor},{especialidad}\n")
            print("Doctor registrado exitosamente\n")

    #Lo que susede si se selecciona la opsion 1
    elif seleccion == 2:

        print("\nModulo de registro de pacientes\n")
        #Preguntas
        carnet = input("Carnet del paciente: ")
        nombre = input("Nombre del paciente: ")
        edad = input("Edad del paciente: ")

        paciente_existe = False

        with open("pacientes.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                #Medida de seguridad por si en caso se deja en blanco un registro
                if len(datos) < 3:
                    continue
                carnet_guardado = datos[0]

                if carnet == carnet_guardado:
                    paciente_existe = True

        if paciente_existe:
            print("El carnet del paciente ya está registrado\n")
        else:
            with open("pacientes.csv", "a") as archivo:
                archivo.write(f"{carnet},{nombre},{edad}\n")
            print("Paciente registrado exitosamente\n")

    elif seleccion == 3:
        #Esto se el pregunta al doctor
        print("\nModulo de registro de horarios\n")
        id_doctor = input("ID del doctor: ")
        fecha = input("Fecha (DD-MM-AAAA): ")
        hora = input("Hora de inicio (HH:MM): ")

        doctor_existe = False

        with open("doctores.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) < 3:
                    continue
                id_guardado = datos[0]
                if id_doctor == id_guardado:
                    doctor_existe = True

        if not doctor_existe:
            print("El doctor no está registrado, por favor verificar ID\n")

        else:
            horario_existe = False

            with open("horarios.csv", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) < 3:
                        continue
                    id_guardado = datos[0]
                    fecha_guardada = datos[1]
                    hora_guardada = datos[2]
                    if id_doctor == id_guardado and fecha == fecha_guardada and hora == hora_guardada:
                        horario_existe = True
            if horario_existe:
                print("Este horario ya está registrado para el doctor\n")
            else:
                with open("horarios.csv", "a") as archivo:
                    archivo.write(f"{id_doctor},{fecha},{hora}\n")
                print("Horario registrado exitosamente\n")

    elif seleccion == 4:
        print("\nModulo de agendar citas\n")

        carnet = input("Carnet del paciente: ")
        id_doctor = input("ID del doctor: ")
        fecha = input("Fecha de la cita (DD-MM-AAAA): ")
        hora = input("Hora de la cita (HH:MM): ")

        paciente_existe = False

        with open("pacientes.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) < 3:
                    continue
                carnet_guardado = datos[0]
                if carnet == carnet_guardado:
                    paciente_existe = True

        if not paciente_existe:
            print("El paciente no está registrado\n")

        else:
            doctor_existe = False
            with open("doctores.csv", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) < 3:
                        continue
                    id_guardado = datos[0]
                    if id_doctor == id_guardado:
                        doctor_existe = True

            if not doctor_existe:
                print("El doctor no existe\n")
            else:
                horario_existe = False

                with open("horarios.csv", "r") as archivo:
                    for linea in archivo:
                        datos = linea.strip().split(",")
                        if len(datos) < 3:
                            continue
                        id_guardado = datos[0]
                        fecha_guardada = datos[1]
                        hora_guardada = datos[2]

                        if id_doctor == id_guardado and fecha == fecha_guardada and hora == hora_guardada:
                            horario_existe = True

                if not horario_existe:
                    print("El doctor no tiene ese horario disponible\n")
                else:
                    cita_ocupada = False

                    with open("citas.csv", "r") as archivo:
                        for linea in archivo:
                            datos = linea.strip().split(",")
                            if len(datos) < 4:
                                continue
                            id_guardado = datos[1]
                            fecha_guardada = datos[2]
                            hora_guardada = datos[3]

                            if id_doctor == id_guardado and fecha == fecha_guardada and hora == hora_guardada:
                                cita_ocupada = True

                    if cita_ocupada:
                        print("Este horario ya está ocupado\n")
                    else:
                        with open("citas.csv", "a") as archivo:
                            archivo.write(f"{carnet},{id_doctor},{fecha},{hora}\n")

                        print("Cita agendada exitosamente\n")

    #Aca solo hay que pedir el carnet del paciente,verificamos que exista el paciente y luego ya le mostramos el historial
    elif seleccion == 5:
        print("\nModulo de historial de consultas por paciente\n")
        carnet = input("Ingrese el carnet del paciente: ")
        
        paciente_existe = False
        nombre_paciente = ""

        # Verificamos que el paciente exista
        with open("pacientes.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) < 3:
                    continue
                if datos[0] == carnet:
                    paciente_existe = True
                    nombre_paciente = datos[1]
                    break

        if not paciente_existe:
            print("El paciente no está registrado\n")
        else:
            print(f"\nHistorial de Citas de: {nombre_paciente} ")
            tiene_citas = False
            
            with open("citas.csv", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) < 4:
                        continue
                    # si el carnet coincide, mostramos la cita
                    if datos[0] == carnet:
                        tiene_citas = True
                        print(f"Doctor ID: {datos[1]} | Fecha: {datos[2]} | Hora: {datos[3]}")
            
            if not tiene_citas:
                print("El paciente no tiene citas registradas.")
            print("\n")

    elif seleccion == 6:
        print("\nModulo de Reporte de citas por doctor y por día\n")
        id_doctor = input("Ingrese el ID del doctor: ").strip()
        fecha_buscada = input("Ingrese la fecha a consultar (DD-MM-AAAA): ").strip()

        doctor_existe = False
        nombre_doctor = ""

        # Verificamos que el doctor exista
        with open("doctores.csv", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) < 3:
                    continue
                if datos[0] == id_doctor:
                    doctor_existe = True
                    nombre_doctor = datos[1]
                    break

        if not doctor_existe:
            print("El doctor no está registrado\n")
        else:
            print(f"\nAgenda del Dr. {nombre_doctor} para el {fecha_buscada}")
            tiene_citas = False

            with open("citas.csv", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) < 4:
                        continue

                    if datos[1] == id_doctor and datos[2] == fecha_buscada:
                        tiene_citas = True
                        print(f"-> Carnet Paciente: {datos[0]} | Hora: {datos[3]}")

            if not tiene_citas:
                print("El doctor no tiene citas agendadas para este día.")
            print("\n")

    elif seleccion == 0:
        print("\nSaliendo del sistema...")

    else:
        print("Opcion no valida\n")