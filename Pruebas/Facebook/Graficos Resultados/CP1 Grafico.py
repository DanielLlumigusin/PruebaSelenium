import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de ejemplo
data = {
    'Modelo': ['ChatGPT', 'Claude', 'Gemini', 'Bing'] ,
    'Error Humano': [0,3,0,8] ,
    'Acierta/Falla': [0,1,0,0] ,
    'Numero de Consultas': [1,4,1,1] 
}

# Crear DataFrame
df = pd.DataFrame(data)

# Gráfico de dispersión con regresión
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Error Humano', y='Numero de Consultas', hue='Modelo', size='Acierta/Falla', data=df)
plt.title('Análisis de Modelos de IA vs Error Humano y Número de Consultas')
plt.xlabel('Error Humano (1-10)')
plt.ylabel('Número de Consultas')
plt.legend(title='Modelo de IA')
plt.show()

# Gráfico de barras para aciertos/fallas por modelo
plt.figure(figsize=(10, 6))
sns.barplot(x='Modelo', y='Acierta/Falla', data=df, estimator=sum, ci=None)
plt.title('Aciertos vs Fallas por Modelo de IA')
plt.xlabel('Modelo de IA')
plt.ylabel('Total de Aciertos')
plt.show()
