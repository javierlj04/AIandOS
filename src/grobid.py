import time
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from grobid_client.grobid_client import GrobidClient

def analyze_pdf(file_path, grobid_client: GrobidClient):
    """
    Procesa un PDF con GROBID y extrae título, resumen, número de figuras y enlaces.
    """
    # Procesa el PDF y obtiene XML TEI
    _, _, xml_data = grobid_client.process_pdf(
        pdf_file=str(file_path),
        service="processFulltextDocument",
        generateIDs=False,
        consolidate_header=True,
        consolidate_citations=False,
        include_raw_citations=False,
        include_raw_affiliations=False,
        tei_coordinates=False,
        segment_sentences=False
    )
    return parse_tei(xml_data)


def parse_tei(xml_string):
    """
    Extrae información relevante de un XML TEI generado por GROBID.
    """
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    tree = ET.fromstring(xml_string)

    # Título
    title_elem = tree.find('.//tei:titleStmt/tei:title', ns)
    title_text = title_elem.text.strip() if title_elem is not None and title_elem.text else "Sin título"

    # Abstract
    abstract_elem = tree.find('.//tei:abstract', ns)
    abstract_text = ''.join(abstract_elem.itertext()).strip() if abstract_elem is not None else ""

    # Conteo de figuras
    figure_count = len(tree.findall('.//tei:figure', ns))

    # Extracción de enlaces
    links = set()
    for tag in tree.findall('.//tei:ref[@target]', ns) + tree.findall('.//tei:ptr[@target]', ns):
        url = tag.get('target')
        if url and url.startswith(('http://', 'https://')) and url != "https://github.com/kermitt2/grobid":
            links.add(url)

    return {
        'title': title_text,
        'abstract': abstract_text,
        'figures_count': figure_count,
        'links': list(links)
    }


def process_all_pdfs(folder_path, grobid_server="http://localhost:8070"):
    """
    Procesa todos los PDFs de una carpeta con GROBID y devuelve la información de cada artículo.
    """
    if grobid_server != "http://localhost:8070":
        print("Esperando que el servidor GROBID esté listo...")
        time.sleep(30)

    try:
        client = GrobidClient(grobid_server=grobid_server)
    except Exception as e:
        print(f"No se pudo inicializar GROBID: {e}")
        sys.exit(1)

    folder = Path(folder_path)
    pdf_list = list(folder.glob("*.pdf"))

    print(f"Se encontraron {len(pdf_list)} archivos PDF.\n")
    results = []

    for idx, pdf_file in enumerate(pdf_list, 1):
        try:
            print(f"[{idx}/{len(pdf_list)}] Procesando {pdf_file.name}...")
            info = analyze_pdf(pdf_file, client)
            info.update({'filename': pdf_file.name, 'paper_id': pdf_file.stem})
            results.append(info)
        except Exception as e:
            print(f"Error procesando {pdf_file.name}: {e}")

    return results