import pandas as pd


def limpiar(df_limpio):
    columnasInteres = ["pH agua:suelo 2,5:1,0", "Fósforo (P) Bray II mg/kg",
                       "Potasio (K) intercambiable cmol(+)/kg"]

    for col in columnasInteres:
        if col in df_limpio.columns:
            # Limpieza de datos
            df_limpio[col] = df_limpio[col].astype(str)
            df_limpio[col] = df_limpio[col].str.replace(',', '', regex=False)
            df_limpio[col] = df_limpio[col].str.replace('<', '', regex=False)
            df_limpio[col] = df_limpio[col].str.replace('>', '', regex=False)


            df_limpio[col] = pd.to_numeric(df_limpio[col], errors='coerce')
        else:
            print(f"Advertencia: La columna {col} no se encuentra en el DataFrame.")

    return df_limpio

