import funcionExam_fmillar as fun

trabajadores = ["Juan Pérez”, ”María García”, ”Carlos López”, ”Ana Martínez”, ”Pedro Rodríguez”, ”Laura Hernández”, ”Miguel Sánchez”, ”Isabel Gómez”, ”Francisco Díaz”, ”Elena Fernández"]


while True:    
    
    print("-----MENU-----")
    print("1) asignar sueldos aleatorios")
    print("2) Clasificar sueldos")
    print("3) Ver estadísticas")
    print("4) Reporte de sueldos")
    print("5) Salir del programa") 

    opcion = int(input("eliga opcion: ")) 

    if opcion == 1:
        fun.asig_sueldo(trabajadores) 
        
    elif opcion == 2:
        fun.clas_sueldo(trabajadores)            
    
    elif opcion == 3:
        fun.estadist(trabajadores)

    elif opcion == 4:
        fun.report_sueldo(trabajadores)
    
    elif opcion == 5:
        print("finalizando programa...")
        print("desarrollado por franco millar")
        print("rut 19.612.157-9")
        break 
        
    else:
        print("opcion invalida, intente otra vez") 