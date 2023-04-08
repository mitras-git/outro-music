# outro-music
An outro-music parody for macOS that instantly puts your Mac to sleep on the beatdrop of Xenogenesis by TheFatRat

Just uncomment out `os.system("sudo shutdown -s now")` to get it to auctually shut down the computer, but with this method you will have to manually enter you password to give sudo access and ruins the experience.
Running the file as is should just put the computer to sleep instantly

# Modules Used:
1. playsound
2. multiprocessing
3. pydub
