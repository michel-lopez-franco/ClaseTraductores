import os


def contar_archivos_python(directorio):
    contador = 0
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".py"):
                contador += 1
    return contador


if __name__ == "__main__":
    ruta = os.getcwd()  # Directorio actual
    total = contar_archivos_python(ruta)
    print(f"Total de archivos Python: {total}")
