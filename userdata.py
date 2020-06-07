#Библиотека данных человеков
#Копипаста библиотеки настроек

#Импортируем функции файлов и проверки по списку из вспомогательной библиотеки
from func import write, read, cont
#Импортируем сторонние библиотеки
import json
#Импорт штук
import preset

#Объявляем пресеты для каждого участника и задаю шаблон для пресетов
global _basic
_basic = {"cookies": 1,
          "deaths": 0,
          "id": 0, #Его уйдишник (не используется) TODO: Убрать
          "PM": 0  #Если человек писал в личку

         }
_data = {}

#Обновление данных
def upd(ad, d): 
    if type(ad) != type("str"):
       ad = str(ad)
    write("userdata/user_%s.pref"%(ad), json.dumps(d))

#Получение данных об участнике. Если нету - создать.
def getdata(peer):
    f = read("userdata/user_%s.pref"%(peer))
    if not f:
        d = _basic
        write("userdata/user_%s.pref"%(peer), json.dumps(d))
    else:
        d = json.loads(f)
    return d

#Получение конкретных данных о человеке
def _scenr(peer, name):
    if type(peer) != type("str"):
       peer = str(peer)
    d = getdata(peer) #Получаем данные

    if not name in d: #Если данные еще не получены
        d[name] = _basic[name]
        write("userdata/user_%s.pref"%(peer), json.dumps(d))
        return d[name]
    else: 
        return d[name]

#Запись конкретных данных о челоевеке
def e_scenr(peer, name, ayd):
    if type(peer) != type("str"):
       peer = str(peer)
    d = getdata(peer) #Получаем данные

    d[name] = ayd #Далее ничего не назначаем, тк мы передаем ссылку на объект
    write("userdata/user_%s.pref"%(peer), json.dumps(d))

def is_operator(peer, ad):
    return preset._scenr(peer, "operator") == ad

def addpoints(ad, count): #ДАТЬ ПОИНТЫ И ПЕЧЕНЬКИ!
    d = getdata(ad)
    #d["goodness"] += count #Поинты_не_нужны
    d["cookies"] += count / 25
    upd(ad, d)

def removepoints(ad, count): #ОТЖАТЬ ПЕЧЕНЬКИ
    d = getdata(ad)
    upd(ad, d)
    d["cookies"] -= count / 5 #Печеньки ОТБЕРУ К ЧЕРТЯМ


