#Библиотека сообщений.

#Имортируем из библиотеки классов класс ответа
from classes import Answer as A
#Импортируем классификатор из функций
from func import classify
#Имортируем получение префикса из библиотеки настроек
from preset import get_prefix
#Импортируем библиотеку обработки команд
import action_list
#Импортируем генератор ответа в личку и оповещение при добавлении в беседу
from generators import gen_PM, gen_intro

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
        if item in i:
            return True
    return False

#Действия
actions = action_list.get()

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
    if "text" in msg and type(msg["text"]) == str and len(msg["text"]) > 0:
#      ^^^^^^^^^^^^^ - Если в сообщении есть текст (всегда, но длина может быть равна нулю)
#                        ^^^^^^^^^^^^^^^^^^^^^^^^ - Если тип переменной текста - строка (чтобы избежать ошибок)
#                                                     ^^^^^^^^^^^^^^^^^^^^ - Если длина текста больше нуля (см. первый пункт)
        t = msg["text"] #Текст сообщения
        if msg["peer_id"] == msg["from_id"]: #Если сообщение отправлено напрямую в личку
                                             #TODO: может вызывать ошибки, починить
            resp.append(A().New(gen_PM(msg["peer_id"]), "send"))
        else:
            pr = get_prefix(msg["peer_id"]) #Получаем префикс для конкретной беседы
            if pr == t[:len(pr)]: #Если сообщение начинается с префикса
                arc = t[len(pr) + 1:].lower().split(" ") #Получаем список слов
                ac = arc[0] #Получаем самое первое слово
                
                #Проверки на команды
                for c in actions:
                    if cont(ac, c.name):
                        try:
                            ans = c.function(msg["peer_id"], len(arc) >= 2 and arc[1] or None) #TODO: возможно, убрать тернарник (либо приделать отдельный тип вопросов)
                            if ans:
                                resp.append(ans)
                        except: #Если недостаточно аргументов и/или что-то пошло не так
                            resp.append(A().New("Что-то пошло не так. Если это важно - сообщите разработчику код ошибки. [INSERT ERROR CODE]", "send"))
                            #TODO: добавить лог ошибок
                        break
    return resp




















#END
#Code by Oria
