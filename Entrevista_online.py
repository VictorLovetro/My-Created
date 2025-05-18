from time import sleep
import pygame
from os import system
from cpf_generator import CPF

system('cls')
print('\33[1m Olá, tudo bem? Esse site foi criado para você achar vaga de emprego de forma mais fácil, seja bem-vindo(a)\n Logo abaixo aparecerá alguma opções')
sleep(3)

while True:
    pygame.init()
    pygame.mixer_music.load('songlofi.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

    saida = input('Digite (S) se deseja sair ou qualquer tecla para continuar: ').lower()

    if saida == 's':
        print('\33[1;31m Você saiu do programa, volte logo \33[1;31m😢')
        break

    entrada = input('Digite [E] se desejar entrar no programa: ').lower()
    system('cls')

    if entrada == 'e':
        system('cls')
        print('\33[1m Você entrou no programa😊')
        sleep(3)
        
        nome = input('\33[1m Digite seu nome completo, por favor: ').title().split()
        print(f'Olá {nome[0]}, em breve irá aparecer algumas perguma perguntas')
        sleep(3)

        idade = str(input('\33[1m Por favor, Digite sua idade para validar: ')).split(' ')
        valor = int(idade[0])
        system('cls')
        print('\33[1;33m Analizando sua idade, um momento...')
        sleep(2)
        system('cls')

        if valor >=18:
            print('\33[4;32m Sua idade foi verificada com sucesso✅')

        else:
            print('\33[4;31m Houve um problema, idade não permitida para se cadastrar❌')
            break
        
        cidade = str(input('\33[1mPor favor, Digite a cidade que você reside:')).title(). strip(' ')
        print('\33[4;34m Carregando...')
        sleep(2)
        print('\33[4;34m Carregando...')
        system('cls')

        if cidade == 'Ribeirão Preto':
            print('\33[4;32 A Cidade foi verificada com sucesso ✅')

        else:
            print('Esse vaga é apenar para a cidade de Ribeirão Preto, \33[4;33m Fique atento para outras vagas 👀')
            break
        
        cpf = str(input('\33[1m Por favor, Digite o seu cpf: '))
        print('\33[4;34m Carregando...')
        sleep(2)
        if CPF.validate(cpf) == True:
            print('\33[1;32m Seu CPF foi verificado com sucesso✅')
        
        else:
            print('Esse CPF não é verdadeiro')
            break

        experiencia = str(input('\33[1m Você possui alguma experiência na área? Sim/Não: ')).lower()

        if experiencia == 'sim':
            print('\33[1;35m Próxima pergunta...')
            sleep(2)

        else:
            print('Não podemos continuar, pois essa vaga precisa ter experiência, \33[4;33m Fique atento para outras vagas 👀')
            break

        system('cls')
        
        anos_experiencia = str(input('\33[1m Por favor, Digite o tempo de experiência que possui: ')).split()
        valor = int(anos_experiencia[0])

        if valor == 2:
            print('\33[4;32m Cotinuaremos com o processo.')

        else:
            print('Precisamos no mínimo de 2 anos de experiência, \33[4;33m Fique atento para outras vagas 👀')
            break

        relato = input('\33[1m Por favor, fale um pouco sobre as suas expência: ')
        confirmacao = input('Deseja confirmar, Sim/Não: ')

        if confirmacao == 'sim':
            print(relato, '\n\33[4;32m Envidado com sucesso✅')
        else:
            print('\33[4;34m Você preferiu não confirmar, não foi enviado❌')
            break

        system('cls')

        print(f'\33[1m Confirmação: nome:{nome} \n idade:{idade} \n cidade:{cidade} \n CPF:{cpf}')

        certo = input('\33[1m Confirme se seus dados acima estão corretos, Sim/Não:').lower()
        print('\33[4;34m Carregando...')
        sleep(3)

        system('cls')

        if certo == 'sim':
            print('\33[4;33m Em breve entraremos em contato, muito obrigado pela inscrição😊')
            break

        else:
            print('\33[4;31m Pelo que parece seus dados estão errado😢, por favor preencha novamente')
