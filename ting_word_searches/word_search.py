def exists_word(word, instance):

    list_result = []
    for data in instance._list:
        with open(data["nome_do_arquivo"], 'r') as file:
            occurrence = []
            for count_item, line in enumerate(file, start=1):
                if word.lower() in line.lower():
                    occurrence.append({"linha": count_item})
            if occurrence:
                list_result.append({
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                })
    return list_result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
