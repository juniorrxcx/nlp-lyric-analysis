# 📝 NLP & Análise de Sentimentos: Discografia da Taylor Swift

Este projeto aplica técnicas de **Processamento de Linguagem Natural (NLP)** para analisar o peso emocional das letras de música da Taylor Swift. Utilizando a biblioteca TextBlob, o algoritmo lê as letras em inglês e calcula a "Polaridade" de cada faixa, classificando-as em um espectro que vai de -1.0 (emoções extremamente negativas/tristes) a +1.0 (emoções extremamente positivas/felizes).

O resultado final é materializado em uma **Visualização de Dados (DataViz)** através de um gráfico de barras divergente, evidenciando o contraste emocional das composições.

## Tecnologias Utilizadas
* **Python 3:** Linguagem base.
* **Pandas:** Estruturação, limpeza e agrupamento dos dados em DataFrames.
* **TextBlob:** Motor de Inteligência Artificial para análise de sentimentos e cálculo de polaridade do texto.
* **Matplotlib:** Geração do gráfico divergente exportado em alta resolução.

## Arquitetura da Solução
1. **Coleta e Limpeza:** Importação de um dataset massivo em `.csv` (via Kaggle) contendo a discografia. Tratamento de *encoding* (`latin-1`) e remoção de valores nulos.
2. **Processamento NLP:** Criação de uma função de pontuação iterando sobre cada linha de letra musical para calcular o índice de positividade/negatividade.
3. **Agregação:** Uso do método `groupby` do Pandas para calcular a média emocional caso existam múltiplas entradas para a mesma faixa.
4. **DataViz:** Extração do *Top 10* faixas mais positivas e o *Top 10* mais negativas, plotadas em um eixo horizontal divergente (Verde = Positivo, Vermelho = Negativo).