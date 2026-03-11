FROM continuumio/miniconda3

# Crea entorno conda test con Python 3.12 y paquetes necesarios
RUN conda create -n test python=3.12 -y \
	&& conda run -n test pip install requests grobid-client wordcloud matplotlib beautifulsoup4

WORKDIR /app

# Copia el código fuente
COPY . .

# Puerto por defecto para Grobid (si se ejecuta el servidor)
EXPOSE 8070

# Comando por defecto usando conda
CMD ["conda", "run", "-n", "test", "python", "-m", "src.main", "--grobid_url", "http://grobid:8070"]