import os

import eel

from engine.features import *

from engine.command import *


def start():
    eel.init("www")

    PlayAssistantSound()

    # os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    # os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    # eel.start('hometry.html', mode='chrome', host='localhost', block=True)
    
    # os.system('start msedge.exe --app="http://localhost:8000/hometry.html"')

    eel.start("hometry.html",mode=None,host='localhost',block=True)