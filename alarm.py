import time
import pygame
import threading

class Alarm:
    def __init__(self): # Initialize the alarm
        pygame.mixer.init()
        pygame.mixer.music.load("data/Thunderstruck.mp3")
    
    def _loop(self): # Loop the alarm sound
        pygame.mixer.music.play(loops=-1)

    def start_alarm(self): # Start the alarm with a fade-in effect
        pygame.mixer.music.set_volume(0.0)
        threading.Thread(target=self._loop, daemon=True).start() # Start the alarm in a separate thread

        for i in range(21):
            volume = i / 20
            pygame.mixer.music.set_volume(volume)
            time.sleep(10)

    def stop_alarm(self): # Stop the alarm
        pygame.mixer.music.stop()