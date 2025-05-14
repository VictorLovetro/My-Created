import pygame
from random import randint
from os import system
while True:
    pygame.init()
    pygame.mixer_music.load('street_fighter.mp3')
    pygame.mixer.music.play()
    print(pygame.event.wait())

    saida =input('Deseja sair [S] ou aperte [E] para entrar:').lower()
    
    system('cls')

    if saida == 's':
        print('Você saiu do programa, volte logo')
        break
    
    if saida == 'e':
        pygame.init()
        pygame.mixer_music.load('tuc.mp3')
        pygame.mixer.music.play()
        input(pygame.event.wait())

    resposta = int(input('Tente adinhar o número de 0 a 5:'))

    aletorio = randint(0,5)
    print (aletorio)
    
    if resposta == aletorio:
        print('Parábens, você acerotou é o número {}'.format(aletorio))
        pygame.init()
        pygame.mixer_music.load('super_mario_bros.mp3')
        pygame.mixer.music.play()
        input(pygame.event.wait())
        break

    else:
        print('Você errou o número, tente novamente')
        pygame.init()
        pygame.mixer_music.load('you_lose.mp3')
        pygame.mixer.music.play()
        input(pygame.event.wait())
        system('cls')
