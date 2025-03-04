import sys
import os
from tabulate import tabulate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.module import filtrarDatos, calcularMedianas

ruta_csv = r"C:\Users\user}\Documents\Universidad\Semestre V\Progra 4\parcial1_suelos\resultado_laboratorio_suelo.csv"

def tomarDatos():
    while True:
        try:
            limite = int(input("Ingrese el número de registros que desea ver (Debe ser menor a 500): "))

            if limite < 500:
                departamento = input("Ingrese el nombre del departamento a buscar: ")
                municipio = input("Ingrese el nombre del municipio: ")
                cultivo = input("Ingrese el cultivo que desea consultar: ")
                break

            print("Error, el número supera el límite (500). Intente nuevamente.")

        except ValueError:
            print("El número tiene que ser un entero. Intente nuevamente.")

    dataFrame = filtrarDatos(ruta_csv, limite, departamento, municipio, cultivo)

    if dataFrame is not None:
        medianas = calcularMedianas(dataFrame)
        if medianas is not None:
            print("Medianas del cultivo consultado:",cultivo)
            print(medianas)
    else:
        print("No se encontraron datos con los filtros ingresados.")
