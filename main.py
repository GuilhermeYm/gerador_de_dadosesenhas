from time import sleep
import os
import random
import threading

def limpar_tela():
    sistema = os.name
    if sistema == 'nt': 
        os.system('cls')

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
                    choice()

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

def start_fun():
    limpar_tela()
    print("========================================")
    print("             MENU PRINCIPAL             ")
    print("========================================")
    sleep(0.5)
def choice():
    while True:  
        try:
            print('Escolha uma das opções')
            sleep(0.5)
            print("[1] - Gerar dados\n[2] - Ver dados\n[3] - Sair do programa")
            option = int(input('Sua opção: '))
            if option == 1: 
                op.option_one()
            elif option == 2: 
                with open('dados.txt', 'r') as file: 
                    conteudo = file.readline()
                    print(conteudo)
                    sleep(0.5)
                    enter = input('Pressione enter para continuar....')
            elif option == 3: 
                print('Até logo :)')
                sleep(0.5)
                enter_two = input('Pressione enter para continuar....')
                break
            # Adicione blocos elif para as outras opções
        except ValueError: 
            print('Coloque um número que seja igual ao das opções')

# Inicie a função choice em uma thread separada
choice_thread = threading.Thread(target=choice)

# Remova os parênteses para evitar a chamada imediata das funções
vars = {'start': start_fun, 'options': choice_thread}

# Inicie a função correta para iniciar o programa
vars['start']()

# Inicie a thread da função choice
vars['options'].start()
