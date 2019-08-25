# Este script tem a finalidade de criar models.py apartir de arquivos .csv automaticamente
# ele ler apenas o cabeçalho com os nomes das colunas, logo em seguida cria um arquivo básico
# com a importação do django.db.models e a classe informada com todos os atributos baseados no
# nome das colunas do arquivo .csv informado na entrada da execução do script

# É útil quando precisa remodelar o scheme do sistema para uma .csv de muitas colunas


import csv

HEADER_CSV = None

try:
    nome_csv = input('Nome do arquivo CSV: ')
    nome_delimiter = input('Tipo de delimitador do arquivo CSV: ')
    with open(nome_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=nome_delimiter)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Os nomes das colunas são{", ".join(row)}')
                # print(row)
                print('\nCabeçalho do arquivo lido com sucesso!\n')
                HEADER_CSV = row
                line_count += 1
                break
except FileNotFoundError:
    print('\nArquivo CSV selecionado não exite!')
    print('Por favor, execulte novamente este script fornecendo corretamente o nome de um arquivo existente.\n')
    exit()


try:
    nome_arquivo = input('Nome do arquivo a ser criado: ')
    nome_model = input('Nome da Classe a ser criada: ')
    arquivo = open(nome_arquivo, 'r+')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')
    # arquivo.writelines(u'Arquivo criado pois nao existia')
    arquivo.writelines(u'from django.db import models \n\n')
    arquivo.writelines(f'class {nome_model}(models.Model):\n')
    # arquivo.writelines(map(lambda s: s + '\t'+'\n', HEADER_CSV))
    arquivo.writelines(
        '\t' + line + ' = models.CharField(max_length=255) \n' for line in HEADER_CSV)

#faca o que quiser
arquivo.close()
