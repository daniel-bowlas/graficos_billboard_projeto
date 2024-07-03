import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iconic_Songs_Dataset.csv")

genre_counts = df['Genre'].value_counts()

plt.figure(figsize=(10, 6))
bars = genre_counts.plot(kind='bar', color='skyblue')
plt.title('Quantidade de Músicas Lançadas por Gênero || 04.01.2024 - Presente')
plt.xlabel('Gênero')
plt.ylabel('Quantidade de Músicas')
plt.xticks(rotation=45, ha='right')

for i in range(len(genre_counts)):
    plt.text(x=i, y=genre_counts[i] + 0.1, s=str(genre_counts[i]), ha='center')

plt.tight_layout()
plt.show()
