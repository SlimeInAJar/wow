import random
from time import sleep
import threading
from pygame import mixer

def event_random():
    n = random.randint(1, 2)
    return n

def play_music(filepath):
    mixer.init()
    mixer.music.load(filepath)
    mixer.music.play()
    
def event_ammount():
    n = random.randint(1, 10)
    return n

def event_mood():
    n = random.randint(1, 2)
    return n

def start_event(ammount, event):
    i = 0
    music_thread = threading.Thread(target=play_music, args=("/sounds/{event}.mp3"))
    for i in range(ammount):
        i+=1
        music_thread.start()
while(1):
    sleep(random.randint(10, 15))
    event = event_random()
    ammount = event_ammount()
    mood = event_mood()
    start_event(ammount, event)
