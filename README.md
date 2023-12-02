# Mediafire-File-Downloader
Este repositorio contiene un script en Python para la descarga automatizada de archivos de Mediafire. Proporciona las URL de los archivos y el script realiza las descargas automáticamente. Respeta los términos de uso de Mediafire al utilizarlo.
![Repo Banner](https://cdn.freebiesupply.com/images/large/2x/mediafire-logo-transparent.png)

<div align="center">

# Downloader_Mediafire

Descargador automático de archivos de Mediafire utilizando Python.

[![GitHub repo size](https://img.shields.io/github/repo-size/percyjhonhuancachambi/Mediafire-File-Downloader)](https://github.com/percyjhonhuancachambi/Mediafire-File-Downloader)
[![GitHub stars](https://img.shields.io/github/stars/percyjhonhuancachambi/Mediafire-File-Downloader)](https://github.com/percyjhonhuancachambi/Mediafire-File-Downloader/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/percyjhonhuancachambi/Mediafire-File-Downloader)](https://github.com/percyjhonhuancachambi/Mediafire-File-Downloader/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

</div>

---
## Requisitos previos:
- Python 3.x instalado en tu sistema.
- El administrador de paquetes `pip` instalado.

## Pasos de instalación:

1. Abre una terminal o línea de comandos en tu sistema.

2. Clona el repositorio de Downloader_Mediafire desde GitHub ejecutando el siguiente comando:

   ```bash
   git clone https://github.com/percyjhonhuancachambi/Mediafire-File-Downloader.git
   Accede al directorio clonado:

bash
Copiar
cd Mediafire-File-Downloader
```

Instala las dependencias necesarias ejecutando el siguiente comando:

bash
Copiar
pip install -r requirements.txt
```
Instrucciones de uso:
Abre el archivo config.json en un editor de texto y configura los siguientes campos:

email: Tu dirección de correo electrónico asociada a tu cuenta de Mediafire.
password: Tu contraseña de Mediafire.
output_dir: La ruta de la carpeta donde deseas guardar los archivos descargados.
Guarda y cierra el archivo config.json.

En la terminal o línea de comandos, ejecuta el siguiente comando para iniciar la descarga de archivos:

bash
Copiar
python main.py
```

El script buscará los enlaces de descarga en el archivo `links.txt` y descargará automáticamente los archivos de Mediafire.

Asegúrate de agregar los enlaces de descarga en el archivo `links.txt`, uno por línea, antes de ejecutar el script.
