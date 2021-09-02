# FUNCAO MENU INICIAL
def menu_inicial() -> str:
    print()
    print('-'*41+'MENU INICIAL'+'-'*41)
    print('''
    [1] – Criar nova tabela
    [2] – Gravar dados na tabela
    [3] – Ler tabela do arquivo
    [4] – Apagar tabela do arquivo
    [5] – Listar dados da tabela em ordem crescente
    [6] – Consultar um registro
    [7] – Inserir novo registro na tabela
    [8] – Apagar registro
    [9] – Listagem total ou filtrada
    [0] – Sair do programa
    ''')
    print('-'*94)
    v = input('Escolha uma opção: ')
    print()
    return v

# FUNCAO VOLTAR AO MENU
def voltar_menu() -> str:
    z = '1'
    while z != '0':
        print()
        y = input('Deseja voltar ao Menu Inicial? (S/N): ')
        if y == 'S' or y == 's':
            x = menu_inicial()
            z = '0'
        elif y == 'N' or y == 'n':
            x = '0'
            z = '0'
        else:
            print('Opção não encontrada. Tente Novamente!')
            z = '1'
    return x
    
# FUNCAO CRIAR TABELA
def criar_tabela(nomeDoRemedio) -> None:
    nomeDoArquivo = nomeDoRemedio + '.csv'
    arquivo = open(nomeDoArquivo, 'w')
    arquivo.write('Planilha de controle acerca dos testes do remédio {}'.format(nomeDoRemedio))
    arquivo.write('\nNome do Paciente\tIdade do Paciente\tO remédio foi eficaz?\tHouve efeitos colaterais graves/não esperados?\n')
    arquivo.close()
    
# FUNCAO GRAVAR TABELA
def gravar_tabela(nomeArquivo) -> str:
    arquivo = open(nomeArquivo+'.csv', 'a')
    v = '1'
    while v != '0':
        print()
        registro = []
        registro.append(input('Digite o nome do paciente: '))
        registro.append(input('Digite a idade do paciente: '))
        registro.append(input('O tratamento com esse remédio foi eficaz? (SIM/NAO): '))
        registro.append(input('Houve efeitos colaterais graves ou não esperados? (SIM/NAO): '))
        registro = '\t'.join(registro)
        arquivo.write(registro)
        arquivo.write('\n')
        z = '1'
        while z != '0':
            print()
            v = input('''
                    [1] - Deseja adicionar outro registro à tabela?
                    [0] - Voltar ao Menu Inicial
                    Digite sua opção: ''')
            if v=='1' or v =='0':
                z = '0'
            else:
                z = '1'
                print('Opção não encontrada. Tente Novamente!')
    print('Sua tabela foi gravada com sucesso!')
    arquivo.close()
    x = menu_inicial()
    return x

# FUNCAO PARA FORMATACAO DA SAIDA
def formatar(lista) -> list:
    for i in range(4):
        maior = 0
        for j in range(len(lista)):
            if len(lista[j][i]) > maior:
                maior = len(lista[j][i])
        for z in range(len(lista)):
            if len(lista[z][i]) != maior:
                lista[z][i] = lista[z][i] + ' '*(maior-len(lista[z][i]))
    return lista
    
# FUNCAO LER TABELA DO ARQUIVO
def ler_tabela(nomeArquivo) -> None:
    arquivo = open(nomeArquivo+'.csv')
    tabela = []
    for linha in arquivo:
        linha = linha.rstrip('\n')
        tabela.append(linha.split('\t'))
    print()    
    print(''.join(tabela[0]).upper())
    tabela = tabela[1:]
    tabela = formatar(tabela)
    for linha in tabela:
        print('  '.join(linha))
    arquivo.close()
    
# FUNCAO APAGAR TABELA DO ARQUIVO
def apagar_tabela(tabela) -> None:
    import os
    print()
    v = input('''
    [1] - Apagar registros da tabela
    [2] - Apagar tabela (O arquivo ficará vazio)
    [3] - Apagar arquivo que guarda a tabela
    Digite sua opção: ''')
    if v == '1':
        criar_tabela(tabela)
        print('Seus registros foram apagados com sucesso!')
    elif v == '2':
        tabela = tabela + '.csv'
        arquivo = open(tabela, 'w')
        arquivo.close()
        print('Sua tabela foi apagada com sucesso!')
    elif v == '3':
        tabela = tabela + '.csv'
        os.remove(tabela)
        print('Seu arquivo foi apagado com sucesso!')
    else:
        print('Opção não encontrada. Tente Novamente!')

# FUNCAO ORDENAR EM ORDEM ALFABETICA
def cmp_alpha(registro1 ,registro2) -> int:
    if registro1[0] < registro2[0]:
        return -1
    elif registro1[0] == registro2[0]:
        return 0
    else:
        return 1

# FUNCAO ORDENAR EM ORDEM CRESCENTE DE IDADE
def cmp_idade(registro1 ,registro2) -> int:
    if eval(registro1[1]) < eval(registro2[1]):
        return -1
    elif eval(registro1[1]) == eval(registro2[1]):
        return 0
    else:
        return 1

# FUNCAO ORDENAR TABELA
def listar_dados_ordenados(nomeTabela) -> None:
    from functools import cmp_to_key
    arquivo = open(nomeTabela +'.csv')
    tabela = []
    for linha in arquivo:
        linha = linha.rstrip('\n')
        tabela.append(linha.split('\t'))
    t1 = tabela[0]
    t2 = tabela[1]
    tabela = tabela[2:]
    arquivo.close()
    print()
    a = input('''Escolha um critério para a ordenação:
     [1] - Ordem alfabética dos nomes dos pacientes
     [2] - Ordem crescente das idades
     Digite sua opção: ''')
    if a == '1':
        tabela.sort(key=cmp_to_key(cmp_alpha))
        tabela = [t2] + tabela
        tabela = formatar(tabela)
        print()
        print(''.join(t1).upper())
        for linha in tabela:
            print(' '.join(linha))
    elif a == '2':
        tabela.sort(key=cmp_to_key(cmp_idade))
        tabela = [t2] + tabela
        tabela = formatar(tabela)
        print()
        print(''.join(t1).upper())
        for linha in tabela:
            print('  '.join(linha))
    else:
        print('Opção não encontrada. Tente Novamente!')

# FUNCAO CONSULTAR REGISTRO
def consultar_registro(nomeArquivo) -> None:
    arquivo = open(nomeArquivo+'.csv')
    tabela = []
    for linha in arquivo:
        linha = linha.rstrip('\n')
        tabela.append(linha.split('\t'))
    print()
    z = input('Digite o nome completo do paciente (Da mesma forma nomeada ao registrá-lo na tabela) para ter acesso ao registro dele: ')
    temp = tabela[1]
    tabela = tabela[2:]
    for i in range(len(tabela)):
        if z == tabela[i][0]:
            tabela = tabela[i]
    tabela = [temp,tabela]
    tabela = formatar(tabela)
    print()
    for linha in tabela:
        print(' '.join(linha))
    arquivo.close()

# FUNCAO APAGAR REGISTRO DA TABELA
def apagar_registro(nomeArquivo) -> None:
    arquivo = open(nomeArquivo+'.csv')
    tabela = []
    for linha in arquivo:
        tabela.append(linha.split('\t'))
    arquivo.close()
    print()
    z = input('Digite o nome completo do paciente (Da mesma forma nomeada ao registrá-lo na tabela) para que esse registro seja apagado: ')
    tabela = tabela[2:]
    for i in range(len(tabela)-1):
        if z == tabela[i][0]:
            del(tabela[i])
    criar_tabela(nomeArquivo)
    arquivo = open(nomeArquivo+'.csv', 'a')
    for linha in tabela:
        linha = '\t'.join(linha)
        arquivo.write(linha)
    arquivo.close()
    print('O registro foi apagado com sucesso!')

    
# FUNCAO FILTRAR LISTA
def listagem_filtrada(tabela,filtro,campo) -> None:
    temp2 = [tabela[1]]
    tabela = tabela[2:]
    for i in range(len(tabela)):
        if filtro in tabela[i][campo]:
            temp2.append(tabela[i])
    if len(temp2) == 1:
        print()
        print('Nenhum paciente atende a condição procurada. Tente Novamente!')
    else:
        print()
        temp2 = formatar(temp2)
        for linha in temp2:
            print(' '.join(linha))

# FUNCAO FILTRAR IDADE
def listagem_filtrada_idade(tabela,filtro) -> None:
    temp2 = [tabela[1]]
    tabela = tabela[2:]
    for i in range(len(tabela)):
        if filtro == eval(tabela[i][1]):
            temp2.append(tabela[i])
    if len(temp2) == 1:
        print()
        print('Nenhum paciente possui a idade procurada. Tente Novamente!')
    else:
        print()
        temp2 = formatar(temp2)
        for linha in temp2:
            print(' '.join(linha))

# FUNCAO LISTAGEM TOTAL OU FILTRADA
def listagem_total_ou_filtrada(nomeArquivo) -> None:
    arquivo = open(nomeArquivo + '.csv')
    tabela = []
    for linha in arquivo:
        linha = linha.rstrip('\n')
        tabela.append(linha.split('\t'))
    arquivo.close()
    print()
    z = input('''
    [1] - Listagem Total da tabela
    [2] - Listagem Filtrada da tabela
    Digite sua opção:
    ''')
    if z == '1':
        ler_tabela(nomeArquivo)
    elif z == '2':
        print()
        z = input('''Filtrar através do campo:
        [1] - Nome
        [2] - Idade
        [3] - Eficácia do remédio
        [4] - Ocorrência de Efeitos Colaterais
        Digite sua opção: ''')
        print()
        if z == '1':
            y = input('Digite o nome ou sobrenome do paciente procurado: ')
            listagem_filtrada(tabela,y,0)
        elif z == '2':
            y = eval(input('Digite a idade do paciente procurado: '))
            listagem_filtrada_idade(tabela,y)
        elif z == '3':
            y = input('Digite se o remédio foi eficaz ou não para o paciente procurado (SIM/NAO): ')
            listagem_filtrada(tabela,y,2)
        elif z == '4':
            y = input('Digite se ocorreram efeitos colaterais ou não para o paciente procurado (SIM/NAO): ')
            listagem_filtrada(tabela,y,3)
        else:
            print('Opção não encontrada. Tente Novamente!')

    else:
        print('Opção não encontrada. Tente Novamente!')


######################################### PROGRAMA PRINCIPAL ########################################
print('='*94)
print('BEM VINDO A PLATAFORMA PARA GERENCIAMENTO DE PLANILHAS DE CONTROLE DAS SUAS PESQUISAS CLÍNICAS')
print('='*94)
x = menu_inicial()
while x != '0':

# CRIAR TABELA
    if x == '1':
        a = input('Digite o nome do remédio testado e uma tabela de mesmo nome será criada para que possa ser preenchida posteriormente: ')
        criar_tabela(a)
        print('Sua tabela foi criada com sucesso e já se encontra em um arquivo de mesmo nome! Escolha a opção 2 no menu inicial e informe o nome deste remédio se deseja preenchê-la com os dados')
        x = voltar_menu()
        
# GRAVAR TABELA
    elif x == '2':
        print('ATENÇÃO: Essa função só é possível para as tabelas já criadas. Caso o senhor(a) não a tenha criado ainda, volte ao menu inicial e escolha a opção 1')
        a = input('''
        [1] - Deseja continuar?
        [2] - Voltar ao Menu Inicial
        Digite sua opção: ''')
        if a == '1':
            a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1) para que o senhor(a) possa preencher sua tabela com os dados dos pacientes participantes da pesquisa: ')
            x = gravar_tabela(a)
        elif a == '2':
            x = menu_inicial()
        else:
            print('Opção não encontrada. Tente Novamente!')
            
# LER TABELA
    elif x == '3':
        print('ATENÇÃO: Essa função só é possível para as tabelas já criadas. Caso o senhor(a) não a tenha criado ainda, volte ao menu inicial e escolha a opção 1')
        a = input('''
        [1] - Deseja continuar?
        [2] - Voltar ao Menu Inicial
        Digite sua opção: ''')
        if a == '1':
            a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1) para que a tabela seja lida: ')
            ler_tabela(a)
            x = voltar_menu()
        elif a == '2':
            x = menu_inicial()
        else:
            print('Opção não encontrada. Tente Novamente!')

# APAGAR TABELA
    elif x == '4':
        a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1): ')
        apagar_tabela(a)
        x = voltar_menu()

# ORDENAR TABELA
    elif x == '5':
        a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1) para que seus dados sejam listados de forma ordenada: ')
        listar_dados_ordenados(a)
        x = voltar_menu()

# CONSULTAR REGISTRO
    elif x == '6':
        a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1): ')
        consultar_registro(a)
        x = voltar_menu()

# INSERIR NOVO REGISTRO NA TABELA
    elif x == '7':
        a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1): ')
        x = gravar_tabela(a)

# APAGAR REGISTRO
    elif x == '8':
        a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1): ')
        apagar_registro(a)
        x = voltar_menu()

# LISTAGEM TOTAL OU FILTRADA
    elif x == '9':
        a = input('Digite o nome do remédio testado (Da mesma forma nomeada na opção 1): ')
        listagem_total_ou_filtrada(a)
        x = voltar_menu()

    else:
        print('Opção não encontrada. Tente Novamente!')
        x = voltar_menu()
    