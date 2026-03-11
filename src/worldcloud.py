from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

abstracts = []

for xml_file in ["xml_output/articulo1.xml", "xml_output/articulo2.xml", ...]:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # Ajusta el path según la estructura de Grobid
    abstract = root.find(".//abstract")
    if abstract is not None:
        abstracts.append(abstract.text)

text = " ".join(abstracts)
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
