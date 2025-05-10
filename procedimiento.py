import pandas as pd

def cargar_datos_csv(ruta):
    return pd.read_csv(ruta)

def libros_mas_prestados(df, cantidad=5):
    return df.sort_values(by='Veces_Prestado', ascending=False).head(cantidad)

def libros_por_autor(df, autor):
    return df[df['Autor'].str.contains(autor, case=False)]

def resumen_general(df):
    return df.describe(include='all')

def filtrar_por_genero(df, genero):
    return df[df['Genero'].str.lower() == genero.lower()]