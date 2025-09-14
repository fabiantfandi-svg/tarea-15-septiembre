import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Función para leer el archivo CSV
def leer_archivo(archivo):
    try:
        # Leer el archivo CSV usando pandas
        data = pd.read_csv(archivo)
        print(f"Archivo '{archivo}' cargado exitosamente.\n")
        return data
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

# Función para generar estadísticas descriptivas
def generar_estadisticas(data):
    print("\nEstadísticas descriptivas:")
    print(data.describe())  # Estadísticas básicas: media, desviación estándar, etc.
    print("\nCorrelaciones entre variables:")
    print(data.corr())  # Correlación entre variables numéricas

# Función para generar gráficos simples
def generar_graficos(data):
    # Histograma de las columnas numéricas
    data.hist(bins=20, figsize=(10, 8))
    plt.suptitle("Histogramas de columnas numéricas")
    plt.show()

    # Gráfico de dispersión entre dos variables numéricas (por ejemplo, 'edad' y 'salario')
    if 'edad' in data.columns and 'salario' in data.columns:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=data['edad'], y=data['salario'])
        plt.title("Gráfico de dispersión: Edad vs Salario")
        plt.show()

    # Gráfico de caja (Boxplot) de una columna numérica (por ejemplo, 'salario')
    if 'salario' in data.columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=data['salario'])
        plt.title("Gráfico de caja: Salario")
        plt.show()

# Función principal
def main():
    archivo = 'data.csv'  # Cambia esto por la ruta de tu archivo CSV
    data = leer_archivo(archivo)

    if data is not None:
        # Generar estadísticas
        generar_estadisticas(data)

        # Generar gráficos
        generar_graficos(data)

if __name__ == "__main__":
    main()
