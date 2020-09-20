import os


def obter_nome_antigo(filename):
    print("[Obtendo nome do item...]")

    dict_itens_old = {"digimon_2020": "digimon_adventure_2020_ep_", "maou_gakuin": "maou_gakuin_no_futekigousha_"}

    for item in dict_itens_old:
        if dict_itens_old[item][0:10] == filename[0:10]:
            return dict_itens_old[item]


def obter_nome_novo(old_filename):
    dict_itens_new = {"digimon_adventure_2020_ep_": "Digimon Adventure (2020) - ",
                      "maou_gakuin_no_futekigousha_": "Maou Gakuin no Futekigousha - "}

    for item in dict_itens_new:
        if item == old_filename:
            return dict_itens_new[item]


def renomear_arquivos(diretorio):
    qtd_arquivos = 0

    for file in os.listdir(diretorio):
        if not os.path.isdir(os.path.join(diretorio, file)):
            filename = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]

            nome_antigo = obter_nome_antigo(filename)
            nome_novo = obter_nome_novo(nome_antigo)

            if filename[0:10] == nome_antigo[0:10]:

                old_filename_ep = filename.split('_')[-1]

                if int(old_filename_ep) < 10:
                    old_filename_ep = "0" + old_filename_ep

                full_new_name = nome_novo + old_filename_ep + extension

                os.rename(file, filename.replace(filename, full_new_name))
                print("\n[O arquivo %s foi renomeado para %s]" % (filename, filename.replace(filename, full_new_name)))
                qtd_arquivos += 1

    print("\n[Execução concluída: %i arquivos renomeados]" % qtd_arquivos)
