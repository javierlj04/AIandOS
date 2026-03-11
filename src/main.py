import os
import time
from src.grobid import analyze_pdf
from grobid_client.grobid_client import GrobidClient, ServerUnavailableException

PDF_DIR = "./dataset"
GROBID_URL = "http://grobid:8070"

def wait_for_grobid(url, retries=10, delay=5):
    for attempt in range(retries):
        try:
            client = GrobidClient(grobid_server=url)
            return client
        except ServerUnavailableException:
            print(f"Grobid no disponible, reintentando en {delay}s... (Intento {attempt+1}/{retries})")
            time.sleep(delay)
    raise RuntimeError("No se pudo conectar con Grobid tras varios intentos.")

def main():
    client = wait_for_grobid(GROBID_URL)
    results = []
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')]
    for i, pdf_name in enumerate(pdf_files, 1):
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        print(f"Procesando {pdf_path}")
        info = analyze_pdf(pdf_path, client)
        results.append(info)
    print(results)

if __name__ == "__main__":
    main()
