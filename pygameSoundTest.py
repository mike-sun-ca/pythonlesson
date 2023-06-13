"""import pygame
pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("C:\Windows\Media\Alarm10.wav")
sounda.play()"""

import pygame.midi as pm
import time


pm.init() # init midi player
player = pm.Output(0)
BPM = 120

def play_note(pitch=60, length=2, velocity=127, instrument='Piano'):
    if instrument == 'Piano':
        player.set_instrument(0)
    player.note_on(pitch, velocity)
    time.sleep(length * 60 / BPM)
    player.note_off(pitch, velocity)

play_note(pitch=65,length=1)
play_note(pitch=65,length=1)
play_note(pitch=65,length=1.5)
play_note(pitch=65,length=0.5)
play_note(pitch=65,length=1)
play_note(pitch=64,length=1)
play_note(pitch=64,length=2)

play_note(pitch=67,length=1)
play_note(pitch=67,length=1)
play_note(pitch=65,length=1)
play_note(pitch=62,length=1)
play_note(pitch=60,length=2)
time.sleep(0.5)
play_note(pitch=55,length=1)
play_note(pitch=55,length=1)
play_note(pitch=64,length=1)
play_note(pitch=62,length=1)
play_note(pitch=60,length=1)
play_note(pitch=55,length=3)

play_note(pitch=55,length=0.5)
play_note(pitch=55,length=0.5)
play_note(pitch=55,length=1)
play_note(pitch=64,length=1)
play_note(pitch=62,length=1)
play_note(pitch=60,length=1)
play_note(pitch=57,length=3)
del player
pm.quit()
