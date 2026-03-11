import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Cargar los abstracts desde el archivo de resultados generado por main.py
RESULTS_PATH = "../output/resultados.json"

with open(RESULTS_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

abstracts = [item.get("abstract", "") for item in data if item.get("abstract")]
text = " ".join(abstracts)

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# Guardar la imagen en archivo
plt.savefig("../output/wordcloud.png", bbox_inches="tight")
print("Nube de palabras guardada en ../output/wordcloud.png")
