from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in range(len(instance)):
        if item == path_file:
            return None

    file_line = txt_importer(path_file)
    dict_data = {
            "nome do arquivo": path_file,
            "qtd_linhas": len(file_line),
            "linhas_do_arquivo": file_line,
        }


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
