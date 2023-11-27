import os 
from time import sleep
import string 
import secrets
from classe import Options, limpar_tela

def limpar_tela():
    sistema = os.name
    if sistema == 'nt': 
        os.system('cls')

def str_to_bool(s):
    s_lower = s.lower()
    if s_lower == 'true': 
        return True
    elif s_lower == 'false': 
        return False
    else: 
        sleep(2)
        print('Por favor responde com True para sim e False para não')
        enter = input('Pressione enter para continuar....')
        inicio()

def create_key(comprimento, incluir_letras=True, incluir_numeros=True, incluir_simbolos=True): 
    sleep(0.5)
    print('==============================')
    print('         GERAR SENHA          ')
    print('==============================')
    caracteres = ''
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    if not caracteres:
        raise ValueError('Pelo menos uma opção deve ser selecionada para gerar uma senha e lembrando que só pode responder com True para sim e False para não')
    senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
    print(f'Senha gerada: {senha}')
    sleep(1)
    option_two = int(input('Você quer escrever a senha em um arquivo? [1] - Sim\n[2] - Não\n'))
    if option_two == 1: 
        limpar_tela()
        sleep(2.5)
        name_file = str(input('Qual será o nome do arquivo?  '))
        with open(f'{name_file}.txt', 'a') as file:
            file.write(f'\nSenha: {senha}')    
    enter = input('Pressione enter para continuar.....')


def inicio():
    while True:
        limpar_tela()
        print('================================')
        print('         MENU PRINCIPAL         ')
        print('================================')
        sleep(0.5)
        print('Escolha a sua opção:\n[1] - Gerar Senha\n[2] - Ver senhas\n[3] - Gerar dados\n[4] - Ver dados\n[5] - Sair do programa')
        option_one = int(input('Sua opção? '))

        if option_one == 1:
            tamanho = int(input('Qual será o tamanho da senha?'))
            letras = str(input('Terá letra na senha? Responda com "True" para sim ou "False" para não: '))
            numeros = str(input('Terá número na senha? Responda com "True" para sim ou "False" para não: '))
            simbolos = str(input('Terá símbolos na senha? Responda com "True" para sim ou "False" para não: '))
            letras_fun = str_to_bool(letras)
            numeros_fun = str_to_bool(numeros)
            simbolos_fun = str_to_bool(simbolos)

            sleep(0.5)
            print('Gerando....')
            sleep(3)
            create_key(comprimento=tamanho, incluir_letras=letras_fun, incluir_numeros=numeros_fun, incluir_simbolos=simbolos_fun)
        elif option_one == 2: 
            file_name = str(input('Qual é o nome do arquivo, onde as senhas se encontram e porfavor coloque .txt no final: '))
            if os.path.isfile(file_name): 
                print('Ok, lendo....')
                sleep(3)
                with open(f'{file_name}','r') as file: 
                    conteudo = file.readlines()
                    print(conteudo)
                    enter = input('Pressione enter para continuar....')
            else: 
                print('O arquivo não existe.')
        elif option_one == 3:
            Options.option_one(0)
        elif option_one == 5:
            print('Até logo :)')
            break
        else:
            print('Escolha uma das opções para continuar.')
            sleep(3)
inicio()    
