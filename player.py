#An attempt to build an audio player with basic functionality

import pygame
import os
from random import randint

music_path = os.getcwd()    #Gets the current working directory
file_array = os.listdir(music_path)
audio_array = []
audio_name = 'default'

for i in range(0, len(file_array)):
    if file_array[i].split('.')[1] == 'mp3':    #Gets all mp3 files
        audio_array.append(file_array[i])

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill([0, 0, 0])
pygame.display.update()
pygame.display.set_caption('Audio Player')

pygame.mixer.init(frequency = 22050, size = -16, channels = 2, buffer = 4096)   #Initializing mixer with basic stuff to avoid sound lag

for i in range(0, len(audio_array)):
    pygame.mixer.music.load(audio_array[i])
    audio_name = audio_array[i].split('.')[0]
    pygame.display.set_caption('Audio Player: ' + audio_name)   #Displaying file name in the window caption
    pygame.mixer.music.play()

    while True:
        if pygame.mixer.music.get_busy():
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
            screen.fill([red, green, blue])     #Displays multi-color transition
            pygame.display.update()
            print('Audio Player is running')
        else:
            print('Audio Player has stopped')

pygame.quit()
