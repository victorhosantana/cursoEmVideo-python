from fileinput import filename
from multiprocessing.connection import wait
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(0, 1000.2, 3000)
pygame.event.wait(10000)
pygame.mixer.music.fadeout(5000)
#parar = input('Digite para parar!')
pygame.event.wait(5500)
