import subprocess,os
from subprocess import PIPE, run
import time
import threading
from config import *
from variables import *

programAllowedToRun=False

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout
def putAppOnTop(windowName):
    command='wmctrl -r "'+windowName+'" -b add,above'
    command2='wmctrl -a "'+windowName+'"'
    os.system(command)
    os.system(command2)

def runApp(pathName, windowName):
    os.system('('+pathName+ ')&')
    time.sleep(3)
    #putAppOnTop()
    putAppOnTop(windowName)
def isAppRunning(name):
    batcmd="ps -a | grep "+name
    
    my_output1 = out(batcmd)
    print(my_output1)
    if(name in my_output1):
        print(name+' is running')
        return True
    else:
        print(name+' is NOT running')
        return False

def killApp(name):
    os.system('killall -9 '+name)

def mainFunction(val):
    while 1:
        a=0
    time.sleep(10)


if(loadConfig()):
    programAllowedToRun=1
else:
    programAllowedToRun=0


def guiAppCheck(val):
    global programAllowedToRun
    while 1:
        if(programAllowedToRun==1):
            try:
                if(isAppRunning(GUI_APP_WINDOW_NAME)):
                    continue
                else:
                    runApp(GUI_APP_PATH,GUI_APP_WINDOW_NAME)
            except Exception as e:
                print('e:',e)

def otherAppsCheck():
    global programAllowedToRun
    while 1:
        if(programAllowedToRun==1):
            try:
                if(isAppRunning(TERMINAL_NAME)):
                    killApp(TERMINAL_NAME)
                if(isAppRunning(FILEMANAGER_NAME)):
                    killApp(FILEMANAGER_NAME)
            except Exception as e:
                print('e:',e)



x1 = threading.Thread(target=mainFunction, args=(1,),daemon=True)
x2 = threading.Thread(target=otherAppsCheck, args=(1,),daemon=True)
x1.start()
x2.start()