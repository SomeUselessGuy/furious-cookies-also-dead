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
#TODO: убрать
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

#Поиск по списку формата "1,2,3,4"
def conts(item, cnt):
    for i in cnt.split(","):
        if item in i:
            return True
    return False

#Поиск по списку формата [1,"2",3,"4"]
def cont(item, cnt):
    for i in cnt:
        if item == i:
            return True
    return False

#Получение имени
import vk
from json import dumps, loads
global vkthing, t_names
vkthing = None #Meh


t_names = read("names.cfg")
if not t_names:
    t_names = "{}"
t_names = loads(t_names)

def getname_init(vkth):
    global vkthing
    vkthing = vkth

def getname(A):
    global vkthing, t_names
    if not str(A) in t_names:
        while True:
            if A > 0:
                try:
                    temp = vkthing.users.get(user_ids = A)
                except vk.exceptions.VkAPIError as err:
                    if err.code == 6:
                        sleep(1.1)
                        continue
                    else:
                        raise
                except:
                    raise
                temp = temp[0]
                name = "%s %s"%(temp["first_name"], temp["last_name"])
            else:
                name = str(A)
            t_names[str(A)] = name
            write("names.cfg", dumps(t_names))
            log("%s теперь часть нашего сообщества!"%(name))
            break
    else:
        name = t_names[str(A)]
    return name




#END
#Code by Oria
