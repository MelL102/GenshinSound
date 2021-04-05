import pyautogui
import os
import time
from pycaw.pycaw import AudioUtilities
import subprocess
import sys
import psutil

def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

count = 0

fw = pyautogui.getWindowsWithTitle('Genshin Impact')

sessions = AudioUtilities.GetAllSessions()


while(True):
    for process in psutil.process_iter():
        if checkIfProcessRunning('GenshinImpact.exe'):
            if fw[0].isMinimized == True and count == 0:
                for session in sessions:
                    volume = session.SimpleAudioVolume
                    if session.Process and session.Process.name() == "GenshinImpact.exe":
                        volume.SetMute(1, None)
                        count = 1

            if fw[0].isMinimized == False and count == 1:
                for session in sessions:
                    volume = session.SimpleAudioVolume
                    if session.Process and session.Process.name() == "GenshinImpact.exe":
                        volume.SetMute(0, None)
                        count = 0
        else:
            print("exit")
            sys.exit(0)
