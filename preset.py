#Библиотека кастомных настроек

#Импортируем функции файлов из вспомогательной библиотеки
from func import write, read
#Импортируем сторонние библиотеки
import json

#Объявляем пресеты для каждой беседы и задаю шаблон для пресетов
global _basic
_basic = {"obsc_l": 1,
          "obsc_warn": 1,
          "obsc_warn_ovrc": 1,
          "obsc_warn_ovrc_limit": 3,
          "lack_of_cookies": 0,
          "prefix": "$s",
          "operator": 0,
          "crowd": []}

#Возвращение int из любого типа
def inta(typ, pre):
    try:
        return int(typ)
    except:
        return _basic[pre]

#Получение пресетов конкретной беседы. Если нет - создать.
def getdata(peer):
    d = {}
    f = read("custom/preset_%s.pref"%(peer))
    if not f:
        d = _basic
        write("custom/preset_%s.pref"%(peer), json.dumps(d))
    else:
        d = json.loads(f)
    return d

#Получение конкретных данных о беседе
def _scenr(peer, name):
    if type(peer) != type("str"):
       peer = str(peer)
    d = getdata(peer) #Получаем данные

    if not name in d: #Если данные еще не получены
        d[name] = _basic[name]
        write("custom/preset_%s.pref"%(peer), json.dumps(d))
        return d[name]
    else: 
        return d[name]

#Запись конкретных данных о беседе
def e_scenr(peer, name, ayd):
    if type(peer) != type("str"):
       peer = str(peer)
    d = getdata(peer) #Получаем данные

    d[name] = ayd #Далее ничего не назначаем, тк мы передаем ссылку на объект
    write("custom/preset_%s.pref"%(peer), json.dumps(d))

#Получение данных
def get_prefix(peer):
    return _scenr(peer, "prefix")

def obscene_l(peer):
    return _scenr(peer, "obsc_l")

def obscene_warn(peer):
    return _scenr(peer, "obsc_warn")

def obscene_warn_overcome(peer):
    return _scenr(peer, "obsc_warn_ovrc")

def obscene_warn_overcome_limit(peer):
    return _scenr(peer, "obsc_warn_ovrc_limit")

def cookies_kick(peer):
    return _scenr(peer, "lack_of_cookies")







#END
#Code by Oria
