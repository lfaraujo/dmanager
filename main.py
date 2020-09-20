import os

from file_backup.backup_manager import inserir_arquivo, inserir_arquivo_lote
from file_renamer.rename_files import renomear_arquivos


def main():
    print("--------------------- File Manager v1.0 --------------------- \n")
    diretorio = str(input("-> Diretório de execução: "))
    os.system("cls")
    print("[1] - Renomear arquivos em lote por diretório\n")
    print("[2] - Inserir arquivos em lote\n")
    print("[3] - Inserir arquivo individual\n")
    opcao = int(input("-> "))
    os.system("cls")

    if opcao == 1:
        print("- O diretório será o mesmo inserido anteriormente?\n")
        print("[1] - Sim\n")
        print("[2] - Não\n")
        diretorio_padrao = int(input("-> "))
        os.system("cls")

        if diretorio_padrao == 1:
            renomear_arquivos(diretorio)
        elif diretorio_padrao == 2:
            novo_diretorio = str(input("-> Diretório de execução: "))
            renomear_arquivos(novo_diretorio)
    elif opcao == 2:
        inserir_arquivo_lote(diretorio)
    elif opcao == 3:
        caminho_arquivo = str(input("-> Caminho do arquivo: "))
        inserir_arquivo(caminho_arquivo)


if __name__ == '__main__':
    main()
