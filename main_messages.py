#Библиотека сообщений.

#Имортируем из классов класс ответа
from classes import Answer as A
#Импортируем классификатор из функций
from func import classify
#Импортируем все генераторы ответов
from generators import *
#Имортируем библиотеку настроек
import preset

#Объявляем глобальную переменную бота
global bot
bot = None

#Инициализация бота
def initialize(tyr):
    global bot
    bot = tyr

#Поиск по списку...
def cont(item, cont):
    for i in cont.split(","):
        if item in cont:
            return True
    return False

#Действия с сообщениями
def proceed(msg):
    #{'message': {'date': 1589454222, 'from_id': 147496111, 'id': 13, 'out': 0, 'peer_id': 147496111, 'text': '123', 'conversation_message_id': 13, 'fwd_messages': [], 'important': False, 'random_id': 0, 'attachments': [], 'is_hidden': False}, 'client_info': {'button_actions': ['text', 'vkpay', 'open_app', 'location', 'open_link'], 'keyboard': True, 'inline_keyboard': True, 'lang_id': 0}
    global bot
    if not bot: #Если бот не инициализирован
        raise "Бота не существует" #Вывести ошибку
    resp = [] #Список ответов
    if "action" in msg: #Если определенное действие содержится в сообщении
        ac = msg["action"]
        if ac["type"] == "chat_invite_user": #Если действие - добавление человека в беседу
            if ac["member_id"] == -bot["id"]: #Если человек - это наш бот
                resp.append(A().New(gen_intro(msg["from_id"], msg["peer_id"]), "send")) #Отправить приветственное сообщение
    if "text" in msg: #Если текст содержится в сообщении (всегда, но проверку оставлю)
                      #TODO: запретить возможность писать боту команды в ЛС
        t = msg["text"]
        pr = preset.get_prefix(msg["peer_id"]) #Получаем префикс для конкретной беседы
        if pr == t[:len(pr)]: #Если сообщение начинается с префикса
                              #TODO: убрать говнокод
            arc = t[len(pr) + 1:].lower().split(" ") #Получаем список слов
            ac = arc[0] #Получаем самое первое слово
            struct = "Опция %s установлена на %s." #Создаем шаблон для вывода лога
            #print(ac)
            #--#
            #Проверки на команды
            #preset.e_scenr - Сохранение значений
            if ac == "помощь":
                resp.append(A().New(gen_help(msg["peer_id"]), "send"))                
            elif cont(ac, "настройки,option,options"):
                resp.append(A().New(gen_options(msg["peer_id"]), "send"))
            #settings
            elif cont(ac, "префикс,преф,prefix,pref"):
                c = ac[1]
                preset.e_scenr(msg["peer_id"], "prefix", c)
                resp.append(A().New(struct%("префикса", c), "send"))
            
            elif cont(ac, "фильтр,фильтры,фильтрация"):
                c = arc[1] == "1"
                preset.e_scenr(msg["peer_id"], "obsc_l", c)
                resp.append(A().New(struct%("фильтра", str(c)), "send"))
            
            elif cont(ac, "предупреждения,предупреждение,алерт,варн,warn,alert"):
                c = arc[1] == "1"
                preset.e_scenr(msg["peer_id"], "obsc_warn", c)
                resp.append(A().New(struct%("автоматической выдачи предупреждений", c), "send"))
        
            elif cont(ac, "автокик,кик,autokick"):
                c = inta(arc[1], "obsc_warn_ovrc_limit")
                preset.e_scenr(msg["peer_id"], "obsc_warn_ovrc", c)
                resp.append(A().New(struct%("автокика", c), "send"))
                
            elif cont(ac, "лимит"):
                c = inta(arc[1], "obsc_warn_ovrc_limit")
                preset.e_scenr(msg["peer_id"], "obsc_warn_ovrc_limit", c)
                resp.append(A().New(struct%("лимита предупреждений", c), "send"))
                
            elif cont(ac, "долг"):
                c = arc[1] == "1"
                preset.e_scenr(msg["peer_id"], "lack_of_cookies", c)
                resp.append(A().New(struct%("долга печенек", c), "send"))
    
            #Fun
            elif cont(ac, "печеньки,cookies"):
                resp.append(A().New("Пока тут ничего нет", "send"))
            elif cont(ac, "рейтинг,score"):
                resp.append(A().New("Пока тут ничего нет", "send"))
            elif cont(ac, "миниигры"): 
                resp.append(A().New("Пока тут ничего нет", "send"))
            



    
    return resp




















#END
#Code by Oria
