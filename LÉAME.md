

Requisitos previos:
- Python 3.x instalado en tu sistema.
- El administrador de paquetes `pip` instalado.

Pasos de instalación:

1. Abre una terminal o línea de comandos en tu sistema.

2. Clona el repositorio de Mediafire-File-Downloader desde GitHub ejecutando el siguiente comando:

   ````bash
   git clone https://github.com/percyjhonhuancachambi/Mediafire-File-Downloader.git
   ```

3. Accede al directorio clonado:

   ````bash
   cd Mediafire-File-Downloader
   ```

4. Instala las dependencias necesarias ejecutando el siguiente comando:

   ````bash
   pip install -r requirements.txt
   ```

Instrucciones de uso:

1. Abre el archivo `config.json` en un editor de texto y configura los siguientes campos:

   - `email`: Tu dirección de correo electrónico asociada a tu cuenta de Mediafire.
   - `password`: Tu contraseña de Mediafire.
   - `output_dir`: La ruta de la carpeta donde deseas guardar los archivos descargados.

2. Guarda y cierra el archivo `config.json`.

3. En la terminal o línea de comandos, ejecuta el siguiente comando para iniciar la descarga de archivos:

   ````bash
   python main.py
   ```

   El script buscará los enlaces de descarga en el archivo `links.txt` y descargará automáticamente los archivos de Mediafire.

   Asegúrate de agregar los enlaces de descarga en el archivo `links.txt`, uno por línea, antes de ejecutar el script.

Eso es todo. Ahora el script de descarga automatizada de archivos de Mediafire debería funcionar en tu sistema. Recuerda revisar y respetar los términos de uso de Mediafire al utilizar el script.