# Esta funcion crea un archivo de texto y devuelve el nombre/ruta en el que se creo el mismo
def create_file(content: str, extension: str):
    file_name = f"C:/Users/wilye/Downloads/pedido.{extension}"
    file = open(file_name, "w")
    file.write(content)
    file.close()

    return file_name
