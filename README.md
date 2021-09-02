# Banco de dados em Python
Pequeno banco de dados feito em Python puro como trabalho para a disciplina de Programação de Computadores I ministrada pelo professor Luis Antonio Kowada na Univesidade Federal Fluminense em 2019/1.

## Objetivo

O objetivo deste projeto era a implementação de um banco de dados feito apenas com a linguagem Python e utilizando arquivos e estruturas como listas e matrizes para simular um banco de dados e treinar o aprendizado da linguagem Python.

## Descrição

A criação de novos medicamentos exige uma longa caminhada que inicia-se com sua invenção, testes em laboratório e em animais (Fase pré-clínica), e posteriormente, pela necessidade do teste em seres humanos antes de se veicular o medicamento, ingressa-se na Fase da Pesquisa Clínica. É nesta fase que são feitos os estudos sobre os efeitos clínicos, farmacológicos e farmacodinâmicos do medicamento nos seres humanos, além de definir seu grau de segurança, eficiêcia e dosagem. 

Durante o estudo, o medicamento é testado em pacientes voluntários e são recolhidos inúmeros dados para que ao final do estudo esses dados possam ser submetidos à apreciação das autoridades regulatórias a fim de obter a aprovação do fármaco ou não. A "PLATAFORMA PARA GERENCIAMENTO DE PLANILHAS DE CONTROLE DAS SUAS PESQUISAS CLÍNICAS" foi criada com o intuito de ajudar pesquisadores e biomédicos a armazenarem e acessarem de forma mais prática as informações de controle sobre os pacientes envolvidos no estudo. A plataforma oferece 9 opções ao usuário e cada uma dessas opções é executada por uma função. São elas: 

* (1) - Criar nova tabela, onde o usuário pode criar um arquivo - de mesmo nome do fármaco -  com uma tabela em branco para posterior preenchimento; 
* (2) - Gravar dados na tabela, onde o usuário pode preencher a tabela com os registros dos pacientes, cada registro contém nome e idade do paciente, eficácia e efeitos colaterais graves causados; 
* (3) - Ler tabela do arquivo, em que o usuário informa o nome da tabela que ele deseja ver e ela é lida do arquivo e mostrada na tela; 
* (4) - Apagar tabela do arquivo, onde o usuário tem 3 opções após escolher uma tabela: 
** Apagar todos os resgistros;
** Apagar a tabela do arquivo (nessa opção o arquivo fica vazio);
** Apagar arquivo que guarda a tabela.
* (5) - Listar dados da tabela em ordem crescente, onde o usuário escolhe uma tabela e seus dados são lidos do arquivo e listados na tela em ordem alfabética ou crescente por idade dependendo da escolha do usuário; 
* (6) - Consultar um registro, onde o usuário escolhe uma tabela e digita o nome completo de um paciente e seu registro é mostrado na tela; 
* (7) - Inserir novo registro na tabela, o usuário informa o nome da tabela e pode adicionar novos registros ao final da tabela já existente; 
* (8) - Apagar registro, o usuário informa o nome da tabela e o nome completo do paciente e seu registro é deletado da tabela; 
* (9) - Listagem total ou filtrada, o usuário escolhe entre listagem total ou filtrada, na total é mostrada a tabela inteira e na filtrada o usuário escolhe um campo e digita um "filtro" para que 
seja mostrado na tela apenas registros que contêm esse "filtro". 

Estão implementados no programa, também, outras funções para "controle" e gerenciamento. São elas:  
* (1) - VoltarMenu, para voltar ao menu ou não; 
* (2) - Formatar, para alinhar as colunas ao escrever na tela; 
* (3) - cmp_alpha e cmp_idade, que são funções para ordenação; 
* (4) - ListagemFiltrada e ListagemFiltradaIdade; 
* (5) - MenuInicial, que é sempre  chamado para mostrar as opções ao usuário. 

Arquivo de exemplo: "Imunoglobulina Monoclonanal X.csv"
