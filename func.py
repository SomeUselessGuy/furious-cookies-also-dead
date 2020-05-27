#Вспомогательная библиотека. Дальнейших комментариев не будет (кроме нескольких)

import os
from random import randint
from time import time as curtime, sleep, gmtime, strftime
from math import floor
#Functions
def read(path): #Get file contents
    if not os.path.exists(path):
        return False
    try:
        file = open(path, "r")
        file_contents = file.read()
        file.close()
        return file_contents
    except FileNotFoundError:
        return False
    except:
        return False
def write(path, data = ""): #Write to file
    try:
        _finpath = os.path.abspath(os.getcwd())
        for i in path.split("/")[0:-1]:
            _finpath += "/" + i
        #print(_finpath)
        if not os.path.exists(_finpath):
            os.makedirs(_finpath)
        file = open(path, "w")
        file.write(data)
        file.close()
        return True
    except Exception as er:
        print("Error (file open) - %s\n%s"%(er, path))
        return False

global randomid
randomid = curtime()
def get_randid():
    global randomid
    randomid += randint(0, 120)
    return randomid

def get_token(): #Токен я вам предоставлять не буду
    return read("token.token")

def format_time():
    return strftime("[%H:%M:%S]", gmtime(curtime() + 3600 * 3))

def log(*data):
    print(format_time(), *data)

def stop(message = None):
    if message:
        log("Выполнение программы завершено. Причина: %s"%(message))
    else:
        log("Выполнение программы завершено.")
    exit()

#Не используется вовсе
global d_delay
d_delay = {}
def delay(type = "basic"):
    if type in d_delay and d_delay[type] > 0:
        log("Таймер %s завершен за %s секунд"%(type, floor((curtime() - d_delay[type]) * 10000) / 10000))
        d_delay[type] = 0
    else:
        log("Таймер \"%s\" запущен"%(type))
        d_delay[type] = curtime()

#Используется в паре мест
def classify(i, t = 0):
    h = int(not(not i))
    if t:
        return ["выключена", "активна"][h]
    else:
        return ["выключен", "активен"][h]
log("Функции загружены!")


#END
#Code by Oria
