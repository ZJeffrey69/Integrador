import procedimiento as proc

ruta = "libros_biblioteca.csv"

# Cargar datos
df = proc.cargar_datos_csv(ruta)

# Mostrar resumen
print("Resumen de los libros en la biblioteca:")
print(proc.resumen_general(df))

# Mostrar los libros más prestados
print("\nTop 5 libros más prestados:")
print(proc.libros_mas_prestados(df))

# Buscar libros por autor
autor = input("\n¿Nombre del autor a buscar?: ")
print(proc.libros_por_autor(df, autor))

# Filtrar libros por género
genero = input("\n¿Género a filtrar?: ")
print(proc.filtrar_por_genero(df, genero))