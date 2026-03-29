import pandas as pd
from textblob import TextBlob

print("Abrindo o diário... digo, carregando as letras da Taylor Swift...\n")

try:
    df = pd.read_csv('letras_taylor_swift.csv', encoding='latin-1')
except FileNotFoundError:
    print("Erro: O arquivo 'letras_taylor_swift.csv' não foi encontrado.")
    exit()


coluna_album = 'album'
coluna_musica = 'track_title'
coluna_letra = 'lyric'


df = df.dropna(subset=[coluna_letra])

print("Lendo e calculando o sentimento de cada música (isso pode levar alguns segundos)...")

def calcular_sentimento(texto):
    """
    Usa o TextBlob para analisar o texto em inglês.
    Retorna a polaridade: -1.0 (muito negativo) a 1.0 (muito positivo)
    """
    analise = TextBlob(str(texto))
    return analise.sentiment.polarity

df['Polaridade_Emocional'] = df[coluna_letra].apply(calcular_sentimento)

if len(df) > 0:
    mais_triste = df.sort_values(by='Polaridade_Emocional').iloc[0]
    mais_feliz = df.sort_values(by='Polaridade_Emocional', ascending=False).iloc[0]

    print("\n--- 💔 Extremos Emocionais da Discografia ---")
    print(f"Música mais NEGATIVA/MELANCÓLICA: '{mais_triste[coluna_musica]}' (Álbum: {mais_triste[coluna_album]})")
    print(f"Nota de Sentimento: {mais_triste['Polaridade_Emocional']:.2f}\n")

    print(f"Música mais POSITIVA/ALEGRE: '{mais_feliz[coluna_musica]}' (Álbum: {mais_feliz[coluna_album]})")
    print(f"Nota de Sentimento: {mais_feliz['Polaridade_Emocional']:.2f}\n")

    print("--- 💿 Ranking de Álbuns (Do mais triste para o mais feliz) ---")
    
    media_album = df.groupby(coluna_album)['Polaridade_Emocional'].mean().sort_values()
    
    for album, nota in media_album.items():
        print(f"Álbum: {album.ljust(20)} | Vibe Média: {nota:.3f}")

else:
    print("Nenhuma letra encontrada para analisar.")