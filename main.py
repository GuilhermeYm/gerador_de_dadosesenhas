import os 
from time import sleep
import string 
import secrets
import random 
import threading


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



class Options: 
    def __init__(self):
        self.option = 0

    def option_one(self): 
        sleep(1)
        limpar_tela()
        sleep(1.5)
        print("========================================")
        print("             GERAR DADOS             ")
        print("========================================")
        sleep(1.5)
        print('[1] - Nome\n[2] - Idades\n[3] - Nacionalidade\n[4] - Relacionamento\n[5] - Estado\n[6] - Tudo\n[7] - Voltar')
        options_two = int(input('Você quer gerar o que? '))
        
        if options_two == 1: 
            try:
                with open('arquivo.txt', 'r') as file:
                    limpar_tela() 
                    conteudo = file.readlines()
                    nomes = conteudo[0].strip().split(',')
                    nome = random.choice(nomes)
                    print(f'Nome: {nome}')
                    print('.....')
                    sleep(0.5)
                    print('Você precisa de mais alguma coisa ')
                    option_three = int(input('[1] - Sim\n[2] - Não\n'))
                    if option_three == 1:
                        option_four = int(input('Mas antes, você quer escrever tudo em um arquivo? [1] - Sim\n [2] - Não\n'))
                        if option_four == 1:
                            with open('dados.txt', 'a') as file: 
                                file.write(f'\n   Nome: {nome}')
                                limpar_tela()
                        else:
                            limpar_tela()
                            self.option_one()

                    else: 
                        option_print = int(input('Você quer escrever tudo em um arquivo? [1] - Sim\n[2] - Não\n'))
                        if option_print == 1:
                            with open('dados.txt','a') as file: 
                                file.write(f'   Nome: {nome}')
                                limpar_tela()
            except ValueError as e:
                print(e)

        elif options_two == 2: 
            try:
                limpar_tela()
                idade = random.randint(14, 50)
                print(f'Idade: {idade}')
                sleep(2)  # Adicionado um tempo de espera antes de retornar ao menu principal
                option_three = int(input('Você precisa de mais alguma coisa? [1] - Sim\n[2] - Não\n '))
                if option_three == 1: 
                        option_four = int(input('Mas antes, você quer escrever tudo em um arquivo? [1] - Sim\n [2] - Não\n'))
                        if option_four == 1:
                            with open('dados.txt', 'a') as file: 
                                file.write(f'\n   Idade: {idade}')
                                limpar_tela()
                        else:
                            limpar_tela()
                            self.option_one()
                else:
                    option_print = int(input('Você quer escrever tudo em um arquivo? [1] - Sim\n[2] - Não\n'))
                    if option_print == 1:
                        with open('dados.txt','a') as file: 
                            file.write(f'\n   Idade: {idade}')
                            limpar_tela()
            except ValueError as e: 
                print(e)

        elif options_two == 3: 
            try: 
                limpar_tela()
                with open('arquivo.txt', 'r') as file: 
                    conteudo = file.readlines()
                    nacionalidades = conteudo[1].strip().split(',')
                    nacionalidade = random.choice(nacionalidades)
                    print(f'Nacionalidade: {nacionalidade}')
                    print('.....')
                    sleep(0.5)
                    print('Você precisa de mais alguma coisa ')
                    sleep(0.5)
                    option_three = int(input('[1] - Sim\n[2] - Não\n'))
                    if option_three == 1:
                        option_four = int(input('Mas antes, você quer escrever tudo em um arquivo? [1] - Sim\n [2] - Não\n'))
                        if option_four == 1:
                            with open('dados.txt', 'a') as file: 
                                file.write(f'\n   Nacionalidade: {nacionalidade}')
                                limpar_tela()
                        else:
                            limpar_tela()
                            self.option_one()

                    else: 
                        option_print = int(input('Você quer escrever tudo em um arquivo? [1] - Sim\n[2] - Não\n'))
                        if option_print == 1:
                            with open('dados.txt','a') as file: 
                                file.write(f'\n   Naciolidade: {nacionalidade}')
                                limpar_tela()
            except ValueError as e:
                print(e)

        elif options_two == 4: 
            limpar_tela()
            estado = ['Namorando', 'Casado', 'Solteiro']
            estado = random.choice(estado)
            print(f'Estado: {estado}')
            option_three = int(input('Precisa de mais alguma coisa ? [1] - Sim\n[2] - Não'))
            if option_three == 1: 
                option_four = int(input('Mas antes, você quer escrever tudo em um arquivo? [1] - Sim\n [2] - Não\n'))
                if option_four == 1:
                    with open('dados.txt', 'a') as file: 
                            file.write(f'   Relacionamento: {estado}')
                            limpar_tela()
                else:
                        limpar_tela()
                        self.option_one()
            else: 
                option_print = int(input('Você quer escrever tudo em um arquivo? [1] - Sim\n[2] - Não\n'))
                if option_print == 1:
                    with open('dados.txt','a') as file: 
                        file.write(f'   Relacionamento: {estado}')
                        limpar_tela()

        elif options_two == 5:
            limpar_tela() 
            with open('arquivo.txt', 'r') as file: 
                conteudo = file.readlines()
                estados_br = conteudo[2].strip().split(',')
                estado_br = random.choice(estados_br)
                print(f'Estado Br: {estado_br}')
                option_three = int(input('Precisa de mais alguma coisa? [1] - Sim\n [2] - Não\n'))
                option_four = int(input('Mas antes você não quer registrar esse dado em um arquivo ? [1] - Sim\n [2] - Não\n'))
                if option_four == 1: 
                    with open('dados.txt', 'a') as file: 
                        file.write(f'   Estado:  {estado_br}')
                        sleep(0.5)
                        limpar_tela()
                else: 
                    limpar_tela()
                    inicio()

        elif options_two == 6: 
            limpar_tela()
            with open('arquivo.txt', 'r') as file: 
                conteudo = file.readlines()
                nomes = conteudo[0].strip().split(',')
                nome = random.choice(nomes)
                idade = random.randint(14, 40)
                nacionalidades = conteudo[1].strip().split(',')
                estados_br = conteudo[2].strip().split(',')
                nacionalidade = random.choice(nacionalidades)
                estado_br = random.choice(estados_br)
                relacionamento = ['Casado', 'Solteiro', 'Namorando']
                relacionamento = random.choice(relacionamento)
                tudo = f'Nome: {nome}\nIdade: {idade}\nNacionalidade: {nacionalidade}\nRelacionamento: {relacionamento}\nEstado:{estado_br}'
                print(tudo)
                sleep(0.5)
                input('Você precisa de mais alguma coisa?')
                sleep(9.5)
                option_three = int(input("Mas antes você quer escrever tudo em um arquivo? [1] - Sim\n[2] - Não\n"))
                if option_three == 1: 
                    with open('dados.txt', 'a') as file: 
                        file.write(tudo)
                        limpar_tela()

op = Options()









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
            op.option_one()
        
        elif option_one == 5:
            print('Até logo :)')
            break
        else:
            print('Escolha uma das opções para continuar.')
            sleep(3)
inicio()    
