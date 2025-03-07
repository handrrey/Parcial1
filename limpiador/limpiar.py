import pandas as pd
import numpy as np

def limpiar(df_limpio):
    columnasInteres = ["pH agua:suelo 2,5:1,0", "Fósforo (P) Bray II mg/kg",
                            "Potasio (K) intercambiable cmol(+)/kg"]

    for col in columnasInteres:

                df_limpio[col] = df_limpio[col].astype(str)
                df_limpio[col] = df_limpio[col].str.replace(',', '')
                df_limpio[col] = df_limpio[col].str.replace('<', '').str.replace('>', '')
    
    return df_limpio