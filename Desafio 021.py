import pygame

pygame.mixer.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()

input("Aperte Enter para parar a música...")
pygame.event.wait()