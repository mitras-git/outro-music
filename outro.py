import os
from playsound import playsound
from multiprocessing import Process
import time

def song():
    playsound("outro.mp3")

def counterLoop():
    counter = 15
    while counter >= 0:
        print("Shutting down in " + str(counter))
        time.sleep(1)
        counter -= 1

if __name__ == '__main__':
    p1 = Process(target=song)
    p1.start()
    p2 = Process(target=counterLoop)
    p2.start()
    p2.join()
    os.system("pmset sleepnow")
#    os.system("sudo shutdown -s now")
    p1.kill()
