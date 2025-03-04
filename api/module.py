import pandas as pd
from tabulate import tabulate
import numpy as np

def filtrarDatos(ruta_csv, numeroRegistros, departamentos, municipios, cultivos):
    try:
        df = pd.read_csv(ruta_csv)

        df['Departamento'] = df['Departamento'].astype(str).str.strip().str.upper()
        df['Municipio'] = df['Municipio'].astype(str).str.strip().str.upper()
        df['Cultivo'] = df['Cultivo'].astype(str).str.strip().str.upper()

        departamentos = departamentos.strip().upper() if departamentos else ""
        municipios = municipios.strip().upper() if municipios else ""
        cultivos = cultivos.strip().upper() if cultivos else ""

        consulta = pd.Series(True, index=df.index)

        if departamentos:
            consulta &= df['Departamento'] == departamentos
        if municipios:
            consulta &= df['Municipio'] == municipios
        if cultivos:
            consulta &= df['Cultivo'] == cultivos

        resultadosDataFrame = df[consulta].head(numeroRegistros)

        if resultadosDataFrame.empty:
            print("No se encontraron resultados con los filtros ingresados.")
            return None

    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None

    columnasMostrar = ['Municipio', 'Departamento', 'Cultivo', 'Topografia']
    columnasCalculo = ["pH agua:suelo 2,5:1,0", "Fósforo (P) Bray II mg/kg", "Potasio (K) intercambiable cmol(+)/kg"]


    columnasTotales = columnasMostrar + columnasCalculo
    resultadosDataFrame = resultadosDataFrame[columnasTotales]

    convertirCSV(resultadosDataFrame)
    mostrarTabla(resultadosDataFrame[columnasMostrar])

    return resultadosDataFrame

def convertirCSV(resultadosDataFrame):
    with open("resultados.csv", "w", encoding='utf-8') as f:
        resultadosDataFrame.to_csv(f, index=False)

def mostrarTabla(resultadosDF):
    if resultadosDF is not None and not resultadosDF.empty:
        print(tabulate(resultadosDF, headers='keys', tablefmt='grid'))
    else:
        print("No hay datos para mostrar.")


def calcularMedianas(resultadosDataFrame):
    try:
        columnasInteres = ["pH agua:suelo 2,5:1,0", "Fósforo (P) Bray II mg/kg",
                           "Potasio (K) intercambiable cmol(+)/kg"]

        df_limpio = resultadosDataFrame

        for col in columnasInteres:

            df_limpio[col] = df_limpio[col].astype(str)
            df_limpio[col] = df_limpio[col].str.replace(',', '')
            df_limpio[col] = df_limpio[col].str.replace('<', '').str.replace('>', '')

        df_numerico = df_limpio[columnasInteres].apply(pd.to_numeric, errors='coerce')

        medianas = df_numerico.median()

        return tabulate([medianas.values], headers=columnasInteres, tablefmt='grid')

    except Exception as e:
        print(f"Error al calcular las medianas: {e}")
        return None
