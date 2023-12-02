import requests
from concurrent.futures import ThreadPoolExecutor

# Lista de enlaces de descarga de MediaFire
enlaces_descarga = [
    "https://www.mediafire.com/file/example_file1.pdf",
    "https://www.mediafire.com/file/example_file2.mp4",
    "https://www.mediafire.com/file/example_file3.jpg",
    # Agrega más enlaces de descarga si es necesario
]

# Función para descargar un archivo dado un enlace de descarga
def descargar_archivo(enlace):
    nombre_archivo = enlace.split("/")[-1]  # Obtener el nombre del archivo del enlace
    print(f"Descargando {nombre_archivo}...")
    response = requests.get(enlace)  # Realizar la solicitud GET al enlace de descarga

    if response.status_code == 200:
        # Guardar el contenido de la respuesta en un archivo local
        with open(nombre_archivo, "wb") as archivo:
            archivo.write(response.content)
        print(f"{nombre_archivo} descargado exitosamente.")
    else:
        print(f"No se pudo descargar {nombre_archivo}. Código de estado: {response.status_code}")

# Crea un ThreadPoolExecutor con un máximo de 5 hilos simultáneos
executor = ThreadPoolExecutor(max_workers=5)

# Itera sobre la lista de enlaces de descarga y envía cada uno al ThreadPoolExecutor
for enlace in enlaces_descarga:
    executor.submit(descargar_archivo, enlace)

# Finaliza el ThreadPoolExecutor
executor.shutdown()