import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('edge-of-night-pippins-song.mp3')
pygame.mixer.music.play()
pygame.event.wait()
