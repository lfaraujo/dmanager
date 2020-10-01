import json
import os


def obter_nome_antigo(filename, old_filenames):
    nome_antigo_padrao = "padrão"

    for item in old_filenames:
        if old_filenames[item][0:10] == filename[0:10]:
            return old_filenames[item]

    return nome_antigo_padrao


def obter_nome_novo(old_filename, new_filenames):
    for item in new_filenames:
        if item == old_filename:
            return new_filenames[item]


def renomear_arquivos(diretorio, old_filenames, new_filenames):
    qtd_arquivos = 0

    for file in os.listdir(diretorio):
        if not os.path.isdir(os.path.join(diretorio, file)):
            filename = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]

            nome_antigo = obter_nome_antigo(filename, old_filenames)
            nome_novo = obter_nome_novo(nome_antigo, new_filenames)

            if filename[0:10] == nome_antigo[0:10]:

                old_filename_ep = filename.split('_')[-1]

                if int(old_filename_ep) < 10 and "0" not in old_filename_ep:
                    old_filename_ep = "0" + old_filename_ep

                full_name = nome_novo + old_filename_ep + extension

                os.rename(os.path.join(diretorio, file), os.path.join(diretorio, full_name))

                qtd_arquivos += 1

    return json.dumps({"fim_execucao": "Execução concluída: %i arquivos renomeados" % qtd_arquivos})
