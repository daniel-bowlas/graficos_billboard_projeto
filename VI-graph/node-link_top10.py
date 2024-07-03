import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

df = pd.read_csv("Iconic_Songs_Dataset.csv")

top_artists = df.groupby('Artist')['Popularity'].mean().nlargest(10).index.tolist()

top_df = df[df['Artist'].isin(top_artists)]

G = nx.DiGraph()

for artist in top_artists:
    G.add_node(artist, node_type='artist')

for album in top_df['Album'].unique():
    G.add_node(album, node_type='album')

for _, row in top_df.iterrows():
    G.add_edge(row['Artist'], row['Album'])

pos = nx.spring_layout(G)

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
