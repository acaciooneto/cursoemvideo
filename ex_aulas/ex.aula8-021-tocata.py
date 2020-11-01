import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load('tocata-em-re-menor.mp3')
pygame.mixer.music.play()
#input('toma essa pedra')
pygame.event.wait()
