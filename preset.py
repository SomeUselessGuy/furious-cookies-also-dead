#Библиотека кастомных настроек

#Импортируем функции файлов из вспомогательной библиотеки
from func import write, read
#Импортируем сторонние библиотеки
import json

#Объявляем пресеты для каждого участника и задаю шаблон для пресетов
global _pres, _basic
_basic = {"obsc_l": 1,
          "obsc_warn": 1,
          "obsc_warn_ovrc": 1,
          "obsc_warn_ovrc_limit": 3,
          "lack_of_cookies": 0,
          "prefix": "$s"}
_pres = {}

#Возвращение int из любой из библиотек
def inta(typ, pre):
    try:
        return int(typ)
    except:
        return _basic[pre]

#Получение пресетов конкретной беседы. Если нет - создать.
def getdata(peer):
    d = {}
    if not peer in _pres:
        f = read("custom/preset_%s.pref"%(peer))
        if not f:
            d = _basic
            write("custom/preset_%s.pref"%(peer), json.dumps(d))
        else:
            d = json.loads(f)
        _pres[peer] = d
    else:
        d = _pres[peer]
    return d

#Получение конкретных данных о беседе
def _scenr(peer, name):
    if type(peer) != type("str"):
       peer = str(peer)
    d = getdata(peer)

    if not name in d:
        d[name] = _basic[name]
        write("custom/preset_%s.pref"%(peer), json.dumps(d))
        _pres[peer] = d
        return d[name]
    else:
        return d[name]

#Запись конкретных данных о беседе
def e_scenr(peer, name, ayd):
    if type(peer) != type("str"):
       peer = str(peer)
    d = getdata(peer)

    d[name] = ayd
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
