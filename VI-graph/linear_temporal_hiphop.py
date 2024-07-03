import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iconic_Songs_Dataset.csv")

hiphop_df = df[df['Genre'] == 'Hip-Hop']

hiphop_df['ReleaseDate'] = pd.to_datetime(hiphop_df['ReleaseDate'])

hiphop_df = hiphop_df.sort_values(by='ReleaseDate')

plt.figure(figsize=(10, 6))
plt.plot(hiphop_df['ReleaseDate'], hiphop_df['Popularity'], marker='o', linestyle='-')
plt.title('Popularidade das Músicas de Hip-Hop ao Longo do Tempo')
plt.xlabel('Data de Lançamento')
plt.ylabel('Popularidade')
plt.xticks(rotation=45)

for i, txt in enumerate(hiphop_df['Popularity']):
    plt.text(hiphop_df['ReleaseDate'].iloc[i], txt, f"{txt}", ha='center', va='bottom')

plt.tight_layout()
plt.show()
