#Список взаимодействий

#Имортируем из библиотеки классов класс действия и ответа
from classes import Action as A, Answer as B
#Импортируем все генераторы ответов
from generators import * #TODO: Починить
#Импортируем библиотеку настроек
import preset

#Создаем шаблон для вывода лога
struct = "Опция %s установлена на %s." 

#Ответы
def g_help(peer = None, arg = "None"):
    return B().New(gen_help(peer), "send")
def g_options(peer = None, arg = "None"):
    return B().New(gen_options(peer), "send")
#settings
def g_pref(peer = None, arg = "None"):
    c = arg
    preset.e_scenr(peer, "prefix", c)
    return B().New(struct%("префикса", c), "send")

def g_filter(peer = None, arg = "None"):
    c = arg == "1"
    preset.e_scenr(peer, "obsc_l", c)
    return B().New(struct%("фильтра", str(c)), "send")

def g_warn(peer = None, arg = "None"):
    c = arg == "1"
    preset.e_scenr(peer, "obsc_warn", c)
    return B().New(struct%("автоматической выдачи предупреждений", c), "send")

def g_kick(peer = None, arg = "None"):
    c = preset.inta(arg, "obsc_warn_ovrc_limit")
    preset.e_scenr(peer, "obsc_warn_ovrc", c)
    return B().New(struct%("автокика", c), "send")
    
def g_limit(peer = None, arg = "None"):
    c = preset.inta(arg, "obsc_warn_ovrc_limit")
    preset.e_scenr(peer, "obsc_warn_ovrc_limit", c)
    return B().New(struct%("лимита предупреждений", c), "send")
    
def g_lack(peer = None, arg = "None"):
    c = arg == "1"
    preset.e_scenr(peer, "lack_of_cookies", c)
    return B().New(struct%("долга печенек", c), "send")

#Fun
def g_cookies(peer = None, arg = "None"):
    return B().New("Пока тут ничего нет", "send")
def g_score(peer = None, arg = "None"):
    return B().New("Пока тут ничего нет", "send")
def g_minigames(peer = None, arg = "None"):
    return B().New("Пока тут ничего нет", "send")

#TODO: remove
from urllib.parse import unquote

Cookie = """\
      _________
    /    .      \ 
   /  .     ,     \ 
  |     *   + .    |
  |   ,   ,         |
   \   ,       .  /
    \ _________ /
""".replace(" ", "  ").replace(" ", " %s"%(unquote('%CD%8F')))

def g_cookie(peer = None, arg = "None"):
    return B().New("Вот вам печенька:\n%s"%(Cookie), "send")

#Возвращение
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
        A("миниигр", g_minigames),
        A("печеньку дайте,печенька,печенье", g_cookie)
    ]
