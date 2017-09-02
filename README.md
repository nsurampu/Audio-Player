# Audio-Player

This is an extremely basic audio player that I have coded as a hobby. This uses the PyGame module for playing the audio files in 
a separate window. The project is under development and is not yet fit for easy/normal usage.

Feel free to contribute to the project. 

Requirements:

1. The application currently uses Python 2. Make sure you update your Python 2.
2. Install PyGame. The repository currently hosts the .tar file for linux. To install PyGame:<br>
    i)  Download the .tar file.<br>
    ii) Extract it and run the setup.py file after installing the required dependancies.<br> 
        The dependencies can be installed using:<br>
        sudo apt-get install python-dev libogg-dev libvorbis-dev libfaad-dev libasound2-dev python-pygame
        
        PS- While installing PyGame, the list of dependencies are shown before an installation confirmation. 
        Install only if the status of all dependencies is shown as 'found'.
        
Usage:

1. After installing the required modules and dependancies, run the application using python player.py
2. Input the complete path of the folder where the music to be played has been stored.
3. The application currently does not support multi-event handling, hence has to be forcefully quit using ctrl+c through the 
   terminal.
