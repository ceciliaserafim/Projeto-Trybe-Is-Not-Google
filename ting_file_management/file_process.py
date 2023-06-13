from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    file_line = txt_importer(path_file)
    dict_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_line),
            "linhas_do_arquivo": file_line,
        }
    instance.enqueue(dict_data)
    return print(dict_data, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    file = instance.dequeue()
    path_file = file["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    try:
        position_data = instance.search(position)
        return sys.stdout.write(str(position_data))
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
