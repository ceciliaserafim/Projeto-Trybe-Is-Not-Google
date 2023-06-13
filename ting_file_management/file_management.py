import sys
# sys.studerr é um objeto que representa o fluxo de erro padrão em Python.
# O objetivo de escrever a mensagem de erro em sys.stderr é fornecer
# informações claras sobre o erro, ou seja, erro personalizado.


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return None

    try:
        with open(path_file) as file:
            return file.read().split("\n")
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return None
