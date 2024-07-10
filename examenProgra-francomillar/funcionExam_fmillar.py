import csv
import random as rd
import statistics as media_geo 

sueldo = {} 

def asig_sueldo(trabajadores): 
    
    

    for trabajador in (trabajadores):
        sueldo_trabajador = rd.randint(300000, 2500000) 
        sueldo[trabajador] = sueldo_trabajador 
        
        print(sueldo)    


def clas_sueldo(trabajadores):
    
    for trabajador in (trabajadores): 
        if sueldo_trabajador < 800000: 
            print(" hla") 

def estadist(trabajadores):
    sueldo_base = {} 
    desc_salud = {sueldo_trabajador * 0.07}
    desc_afp = {sueldo_trabajador * 0.12}
    sueldo_liquido = {sueldo_base - desc_salud - desc_afp} 

    
    sueldo_mayor = {}
    sueldo_menor = {} 
    prom_sueldo = {}
    media_geom = {} 
    

    
    sueldo_mayor = max(sueldo) 
    sueldo_menor = min(sueldo) 
    prom_sueldo = sum(sueldo) * len(trabajadores) 
    media_geom = media_geo(sueldo_base) 
    

def report_sueldo(trabajadores): 
    with open ("reporte.csv", "w", newline=' ') as archivoCSV:
        escritor = csv.writer(archivoCSV) 

 
