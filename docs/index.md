# AIandOS
[![DOI](https://zenodo.org/badge/1155343244.svg)](https://doi.org/10.5281/zenodo.18958064)

[![Documentation](https://readthedocs.org/projects/aiandos/badge/?version=latest)](https://aiandos.readthedocs.io/en/latest/)

### Descripción
El repositorio permite analizar y extraer información de papers, visualizar las figuras de los papers y crear una lista de enlaces que se encuentran en cada artículo

### Instrucciones de instalación
Clonar el repositorio:
`git clone https://github.com/javierlj04/AIandOS.git`
`cd AIandOS`

### Requerimientos
- Pyhton >= 3.12
- Docker
- Miniconda3
  - `https://www.anaconda.com/docs/getting-started/miniconda/install`
- Grobid
  - `docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.2`

### Instrucciones de ejecución con Docker
- Tener los archivos pdf en el directorio `dataset`
- Ejecutar el siguiente comando en la terminal en el directorio `AIandOS`:
  `docker compose up`
- La ejecución puede tardar un par de minutos dependiendo de la cantidad de pdfs.
La aplicación devolverá la extracción en la propia terminal (pendiente de actualizar para visualizar las figuras de los papers)

Para cerrar la aplicación se puede hacer usando `docker compose down`

Si no se va a volver a usar la imagen creada con docker se puede eliminar usando `docker rmi aiandos-aiandos:latest`

### Cita preferida
Javier de la Luna Jimenez, J. (2026). Individual Assessment 1 (Version 1.0) [Computer software]. https://github.com/javierlj04/AIandOS

### Si necesita ayuda
https://github.com/javierlj04/AIandOS/issues
