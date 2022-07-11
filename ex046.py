from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('fogos.mp3')
print('\033[95mIniciando contagem regressiva!!!\033[m')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print("\033[95mFogo!!!\033[m")
pygame.mixer.music.play()
input()
