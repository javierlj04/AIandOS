import requests
from grobid import process_pdf_with_grobid
from grobid_client.grobid_client import GrobidClient

URL_FILE = "../dataset/papers.txt"
GROBID_URL = "http://localhost:8070"


def read_urls():
    with open(URL_FILE) as f:
        return [line.strip() for line in f if line.strip()]


def main():

    urls = read_urls()
    client = GrobidClient(grobid_server=GROBID_URL)

    results = []

    for i, url in enumerate(urls, 1):

        print(f"Processing {url}")

        response = requests.get(url)

        temp_pdf = f"temp{i}.pdf"

        with open(temp_pdf, "wb") as f:
            f.write(response.content)

        info = process_pdf_with_grobid(temp_pdf, client)
        results.append(info)

    print(results)


if __name__ == "__main__":
    main()
