#An attempt to build an audio player with basic functionality. Feel free to contribute

import pygame
import os
from random import randint

music_path = raw_input('Enter the complete path of required music folder: ')
file_array = os.listdir(music_path)
audio_array = []

for i in range(0, len(file_array)):
    if file_array[i].split('.')[1] == 'mp3':    #This will get all the mp3 files in the folder
        audio_array.append(file_array[i])

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill([0, 0, 0])
pygame.display.update()
pygame.display.set_caption('Audio Player')

pygame.mixer.init(frequency = 22050, size = -16, channels = 2, buffer = 4096)   #initialising the mixer with a few basic stuff to avoid sound lag

for i in range(0, len(audio_array)):
    pygame.mixer.music.load(audio_array[i])
    pygame.mixer.music.play()

    while True:     #This loop ensures that music is played in the current version of the application
        if pygame.mixer.music.get_busy():
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
            screen.fill([red, green, blue])     #This results in rapid multi-color transitions while the song is being played
            pygame.display.update()
            print('Audio Player is running')
        else:
            print('Audio Player has stopped')

pygame.quit()
