import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

print("Iniciando a análise emocional profunda das letras...")

df = pd.read_csv('letras_taylor_swift.csv', encoding='latin-1')
coluna_musica = 'track_title'
coluna_letra = 'lyric'
df = df.dropna(subset=[coluna_letra])

def calcular_sentimento(texto):
    return TextBlob(str(texto)).sentiment.polarity

print("Lendo e pontuando cada música (isso leva alguns segundos)...")
df['Polaridade'] = df[coluna_letra].apply(calcular_sentimento)

df_musicas = df.groupby(coluna_musica)['Polaridade'].mean().reset_index()

df_ordenado = df_musicas.sort_values(by='Polaridade')
top_10_negativas = df_ordenado.head(10)
top_10_positivas = df_ordenado.tail(10)

df_grafico = pd.concat([top_10_negativas, top_10_positivas])

print("Desenhando o Gráfico Divergente...")

plt.figure(figsize=(12, 8))

cores = ['#d62728' if nota < 0 else '#2ca02c' for nota in df_grafico['Polaridade']]

plt.barh(df_grafico[coluna_musica], df_grafico['Polaridade'], color=cores, edgecolor='black', alpha=0.8)

plt.title('Extremos Emocionais da Taylor Swift (Análise de Letras com NLP)', fontsize=16, pad=20)
plt.xlabel('Peso Emocional (Polaridade: -1.0 Triste a 1.0 Feliz)', fontsize=12)
plt.ylabel('Músicas', fontsize=12)

plt.axvline(0, color='black', linewidth=1.5, linestyle='-') 
plt.grid(axis='x', linestyle='--', alpha=0.5)

plt.tight_layout()

nome_grafico = 'grafico_divergente_taylor.png'
plt.savefig(nome_grafico, dpi=300)

print(f"Sucesso absoluto! O gráfico foi salvo na sua pasta como '{nome_grafico}'.")