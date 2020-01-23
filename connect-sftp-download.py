#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pysftp


host = 'teste'
username = 'teste'
password = 'teste'
cnopts = pysftp.CnOpts()  # Cria as Options da Conexao SFTP
cnopts.hostkeys = None  # Define as Options da Conexao SFTP


# [ Conecta ao SFTP ]
with pysftp.Connection(host=str(host), username=str(username), password=str(password), cnopts=cnopts) as sftp:

    # Navega para o Diretorio dos Arquivos
    sftp.cwd('bases/01-01-2020')

    # Obtem a 'estrutura' dos Arquivos do Diretorio Remoto
    files_structure = sftp.listdir_attr()

    # [ Para cada 'estrutura' de Arquivo no Diretorio Remoto ]
    for file in files_structure:
        try:
            # OBS1: "str(file).split()" Retorna o Array:  ['Permissao', 'Numero(?)', 'PIDdoUsuario(?)', 'GrupoDoUsuario(?)', 'TamanhoDoArquivo', 'Dia', 'Mes', 'Hora:Minuto', 'NomeDoArquivo']
            # OBS2: E possivel retornar dados especificos do Objeto do Arquivo consultando diretamente seus seguintes Atributos:  file.st_size = 'TamanhoDoArquivo', file.st_uid = 'PIDdoUsuario(?)', file.st_gid = 'GrupoDoUsuario(?)', file.st_mode = 'Modo(?)', file.st_atime = 'TemestampDoUltimoAcesso', file.st_mtime = 'TimestampDaUltimaModificacao', file.filename = 'NomeDoArquivo'

            # [ Efetua o Download do Arquivo ]
            try:
                remoteFilePath = 'bases/01-01-2020/'+str(file.filename)  # Define o Arquivo que sera baixado do Diretorio remoto
                localFilePath = './_BASES/'+str(file.filename)  # Define o local onde o Arquivo sera salvo
                sftp.get(remoteFilePath, localFilePath)  # Efetua o Download do Arquivo

            except Exception as E:
                print('Erro ao Efetuar o Download do Arquivo.')
                print(str(E))
                continue

        except Exception as E:
            print('Erro no Loop do FOR.')
            print(str(E))
            continue
