#Список взаимодействий

#Имортируем из библиотеки классов класс действия и ответа
from classes import Action as A, Answer as B
#Импортируем все генераторы ответов
from generators import * #TODO: Починить
#Импортируем библиотеку настроек и человеков
import preset, userdata
#Флур
from math import floor
#Получение имени
from func import getname

#Создаем шаблон для вывода лога
struct = "Опция %s установлена на %s." 

#Ответы
def g_help(peer = None, arg = "None", sender = None):
    return B(gen_help(peer), "send")
def g_options(peer = None, arg = "None", sender = None):
    return B(gen_options(peer), "send")
#settings
def g_pref(peer = None, arg = "None", sender = None):
    c = arg
    preset.e_scenr(peer, "prefix", c)
    return B(struct%("префикса", c), "send")

def g_filter(peer = None, arg = "None", sender = None):
    c = arg == "1"
    preset.e_scenr(peer, "obsc_l", c)
    return B(struct%("фильтра", str(c)), "send")

def g_warn(peer = None, arg = "None", sender = None):
    c = arg == "1"
    preset.e_scenr(peer, "obsc_warn", c)
    return B(struct%("автоматической выдачи предупреждений", c), "send")

def g_kick(peer = None, arg = "None", sender = None):
    c = preset.inta(arg, "obsc_warn_ovrc_limit")
    preset.e_scenr(peer, "obsc_warn_ovrc", c)
    return B(struct%("автокика", c), "send")
    
def g_limit(peer = None, arg = "None", sender = None):
    c = preset.inta(arg, "obsc_warn_ovrc_limit")
    preset.e_scenr(peer, "obsc_warn_ovrc_limit", c)
    return B(struct%("лимита предупреждений", c), "send")
    
def g_lack(peer = None, arg = "None", sender = None):
    c = arg == "1"
    preset.e_scenr(peer, "lack_of_cookies", c)
    return B(struct%("долга печенек", c), "send")

#Fun
def g_cookies(peer = None, arg = "None", sender = None):
    return B("У вас %s печенек!"%(floor(userdata._scenr(sender, "cookies"))), "send")
def g_score(peer = None, arg = "None", sender = None):
    txt = "Рейтинг самых богатых печеньевых магнатов:\n"
    #СортировОчка
    arr = []
    for i in preset._scenr(peer, "crowd"):
        g = userdata._scenr(i, "cookies") #Сохраняем печеньки в отдельную переменную
        used = False #Прок
        for i1 in range(len(arr)):
            if arr[i1][1] <= g: #TODO: Возможно, перекодить
                arr.insert(i1, [i, g])
                used = True
                break
        if not used:
            arr.append([i, g])
    #Тут кончается сортировОчка
    h = 1
    for i in arr:
        txt += "%s - %s - %s печеньки.\n"%(h, getname(i[0]), floor(i[1]))
        h += 1
        if h >= 11:
            break
    return B(txt, "send")
def g_minigames(peer = None, arg = "None", sender = None):
    return B("Пока тут ничего нет", "send")

#Назначение оператора
def g_operator(peer = None, arg = "None", sender = None):
    if peer and sender:
        preset.e_scenr(peer, "operator", sender)
        return B("[id%s|Этот] человек назначен оператором данной беседы."%(sender), "send")

#Возвращение
#Для бесед
def get():
    return [
        A("помощь", g_help),
        A("настройки,option,options", g_options),
        A("префикс,преф,prefix,pref", g_pref),
        A("фильтр,фильтры,фильтрация", g_filter),
        A("предупреждения,предупреждение,алерт,варн,warn,alert", g_warn),
        A("автокик,кик,autokick", g_kick),
        A("лимит", g_limit),
        A("долг", g_lack),
        A("печеньки,cookies", g_cookies),
        A("рейтинг,score", g_score),
        A("миниигры", g_minigames),
        A("оператор,опка", g_operator)
    ]

##PM PART##

def g_PM(peer = None, arg = "None"):
    return B(gen_PM(0), "send")








#Возвращение
#Для отдельных людей (личка)
#TODO: убрать, тк не используется (либо заменить другим аналогом)
def get_pm():
    return [
        A("start", g_PM),
        A("беседы", g_PM)
    ]