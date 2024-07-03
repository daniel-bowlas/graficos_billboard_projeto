import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Carregar o dataset
df = pd.read_csv("Iconic_Songs_Dataset.csv")

# variavel top 10 artistas com mais popularidade
top_artists = df.groupby('Artist')['Popularity'].mean().nlargest(10).index.tolist()

# filtro DataFrame apenas para os top 10 artistas
top_df = df[df['Artist'].isin(top_artists)]

# grafo direcionado
G = nx.DiGraph()

# nós - artistas
for artist in top_artists:
    G.add_node(artist, node_type='artist')

# nós - álbuns
for album in top_df['Album'].unique():
    G.add_node(album, node_type='album')

# arestas artistas - álbuns
for _, row in top_df.iterrows():
    G.add_edge(row['Artist'], row['Album'])

# Layout do grafo
pos = nx.spring_layout(G)

# Plotar o gráfico do grafo de top 10 artistas e álbuns
plt.figure(figsize=(12, 8))
artists = [node for node in G.nodes() if G.nodes[node]['node_type'] == 'artist']
albums = [node for node in G.nodes() if G.nodes[node]['node_type'] == 'album']
nx.draw_networkx_nodes(G, pos, nodelist=artists, node_color='skyblue', node_size=3000, alpha=0.8)
nx.draw_networkx_nodes(G, pos, nodelist=albums, node_color='lightgreen', node_size=1000, alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10)
plt.title('Top 10 Artistas e Seus Respectivos Álbuns')
plt.axis('off')
plt.show()

# filtro apenas das músicas do gênero "Hip-Hop"
hiphop_df = df[df['Genre'] == 'Hip-Hop']

# coluna 'ReleaseDate' para o formato de data
hiphop_df['ReleaseDate'] = pd.to_datetime(hiphop_df['ReleaseDate'])

# ordenar o DataFrame por data de lançamento
hiphop_df = hiphop_df.sort_values(by='ReleaseDate')

# gráfico linear da popularidade ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(hiphop_df['ReleaseDate'], hiphop_df['Popularity'], marker='o', linestyle='-')
plt.title('Popularidade das Músicas de Hip-Hop ao Longo do Tempo')
plt.xlabel('Data de Lançamento')
plt.ylabel('Popularidade')
plt.xticks(rotation=45)

# rótulos em cada ponto
for i, txt in enumerate(hiphop_df['Popularity']):
    plt.text(hiphop_df['ReleaseDate'].iloc[i], txt, f"{txt}", ha='center', va='bottom')

plt.tight_layout()
plt.show()

# número de músicas para cada gênero
genre_counts = df['Genre'].value_counts()

# gráfico de barras
plt.figure(figsize=(10, 6))
bars = genre_counts.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Músicas Lançadas por Gênero || 04.01.2024 - Presente')
plt.xlabel('Gênero')
plt.ylabel('Quantidade de Músicas')
plt.xticks(rotation=45, ha='right')

# rótulos de texto acima de cada barra
for i in range(len(genre_counts)):
    plt.text(x=i, y=genre_counts[i] + 0.1, s=str(genre_counts[i]), ha='center')

plt.tight_layout()
plt.show()
