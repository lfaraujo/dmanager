import os
import time

import mysql.connector

from config.database_config import CONNECTION_CONFIG


def abrir_conexao(host, database, user, password):
    try:
        connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        return connection
    except mysql.connector.Error as error:
        print("Falha ao abrir conexão: {}".format(error))


def obter_conteudo_arquivo(nome_arquivo):
    with open(nome_arquivo, 'rb') as arquivo:
        conteudo_arquivo = arquivo.read()

    return conteudo_arquivo


def existe_arquivo_base(nome):
    conn = abrir_conexao(CONNECTION_CONFIG["host"], CONNECTION_CONFIG["database"], CONNECTION_CONFIG["user"],
                         CONNECTION_CONFIG["password"])

    cursor = conn.cursor()

    query_validacao = """ SELECT id FROM video WHERE REPLACE(nome, '''', '') = REPLACE('{}', '''', '') """.format(nome)

    cursor.execute(query_validacao)

    id_item = cursor.fetchall()

    if id_item is None or not id_item:
        cursor.close()
        conn.close()
        return False
    else:
        cursor.close()
        conn.close()
        return True


def tratar_nome(nome):
    if "'" in nome:
        return nome.replace("'", "''")

    return nome


def inserir_arquivo(arquivo):
    conn = abrir_conexao(CONNECTION_CONFIG["host"], CONNECTION_CONFIG["database"], CONNECTION_CONFIG["user"],
                         CONNECTION_CONFIG["password"])

    cursor = conn.cursor()

    nome = tratar_nome(os.path.basename(arquivo))
    conteudo = obter_conteudo_arquivo(arquivo)

    if not existe_arquivo_base(nome):
        query_insert = """ INSERT INTO video (nome, conteudo) VALUES (%s, %s) """
        tuple_insert = (nome, conteudo)

        print("[Inserindo o item: %s]" % nome)

        start_time = time.perf_counter()

        cursor.execute(query_insert, tuple_insert)
        conn.commit()
        cursor.close()
        conn.close()

        elapsed_time = int(time.perf_counter() - start_time)

        print("[Conteúdo inserido: %s - %i bytes - duração: %s segundos]" % (
            nome, os.path.getsize(arquivo), elapsed_time))

    else:
        print("[Pulando arquivo: %s]" % nome)


def inserir_arquivo_lote(diretorio):
    pastas = [os.path.join(diretorio, nome) for nome in os.listdir(diretorio)]
    arquivos = []
    aux = 0

    while aux < len(pastas):
        item = pastas[aux]

        for conteudo in os.listdir(item):
            if conteudo.lower().endswith(".mp4"):
                arquivos.append(os.path.join(item, conteudo))
            elif os.path.isdir(os.path.join(item, conteudo)):
                pastas.append(os.path.join(item, conteudo))

        aux += 1

    for arquivo in arquivos:
        inserir_arquivo(arquivo)
