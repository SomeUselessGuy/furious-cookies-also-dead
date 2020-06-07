#Библиотека сообщений.

#Имортируем из библиотеки классов класс ответа
from classes import Answer as A
#Импортируем классификатор, поиск по списку и случайный номер из функций
from func import classify, cont, conts, get_randid as randid, log
#Имортируем библиотеку настроек
import preset
#Импортируем библиотеку обработки команд
import action_list
#Импортируем генератор ответа в личку и оповещение при добавлении в беседу
from generators import gen_PM, gen_intro
#Импортируем обработчик "обычных" сообщений
import simple_messages as messages
#Импортируем библиотеку сущест*зачеркнуто* человеков
import userdata

#Объявляем глобальную переменную бота
global bot, vkthing
bot = None
vkthing = None

#Инициализация бота
def initialize(tyr, _vk):
    global bot, vkthing
    bot = tyr
    vkthing = _vk

#Действия
actions_chat = action_list.get()
actions_pm = action_list.get_pm()

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
                resp.append(A(gen_intro(msg["from_id"], msg["peer_id"]), "send")) #Отправить приветственное сообщение
    if "text" in msg and type(msg["text"]) == str and len(msg["text"]) > 0 and msg["peer_id"] > 0:
#      ^^^^^^^^^^^^^ - Если в сообщении есть текст (всегда, но длина может быть равна нулю)
#                        ^^^^^^^^^^^^^^^^^^^^^^^^ - Если тип переменной текста - строка (чтобы избежать ошибок)
#                                                     ^^^^^^^^^^^^^^^^^^^^ - Если длина текста больше нуля (см. первый пункт)
#                                                                              ^^^^^^^^^^^^^^^^^^ - Если сообщение отправленно НЕ сообществом
        t = msg["text"] #Текст сообщения
        if msg["peer_id"] == msg["from_id"]: #Если сообщение отправлено напрямую в личку
                                             #TODO: может вызывать ошибки, починить
            if userdata._scenr(msg["from_id"], "PM") == 0:
                userdata.e_scenr(msg["from_id"], "PM", 1)
                resp.append(A(gen_PM(msg["peer_id"]), "send"))
        else:
            prfr = preset._scenr(msg["peer_id"], "crowd")
            if not cont(msg["from_id"], prfr):
                prfr.append(msg["from_id"])
                preset.e_scenr(msg["peer_id"], "crowd", prfr)
            pr = preset.get_prefix(msg["peer_id"]) #Получаем префикс для конкретной беседы
            if pr == t[:len(pr)]: #Если сообщение начинается с префикса
                arc = t[len(pr) + 1:].lower().split(" ") #Получаем список слов
                ac = arc[0] #Получаем самое первое слово
                
                #Проверки на команды
                for c in actions_chat:
                    if conts(ac, c.name):
                        try:
                            ans = c.function(msg["peer_id"], len(arc) >= 2 and arc[1] or None, msg["from_id"]) #TODO: возможно, убрать тернарник (либо приделать отдельный тип вопросов)
                            if ans:
                                resp.append(ans)
                        except Exception as er: #Если недостаточно аргументов и/или что-то пошло не так
                            resp.append(A("Что-то пошло не так. Если это важно - сообщите разработчику код ошибки. [INSERT ERROR CODE]", "send"))
                            print(er)
                            #TODO: добавить лог ошибок
                        break
            else: #Если это обычное сообщение
                rest = messages.nice(msg["text"]) #Не передаем отправителя чтобы у нас была честная и прозрачная система
                if not userdata.is_operator(msg["peer_id"], msg["from_id"]): #Проверяем отправителя, чтобы у нас не было честной и прозрачной системы
                    if rest["points"] < 0:
                        userdata.removepoints(msg["from_id"], rest["points"]) #Забираем у пользователя кол-во поинтов
                    elif rest["points"] > 0:
                        userdata.addpoints(msg["from_id"], rest["points"]) #Даем пользователю кол-во поинтов

    return resp

def operator(peer, text): #Постучать оператору беседы в личку
    op = preset._scenr(peer, "operator")
    if op > 0:
        try:
            vkthing.messages.send(peer_id = op, message = text, random_id = randid())
        except Exception as er: #TODO: изменить
            log(str(er))
            preset.e_scenr(peer, "operator", 0)
            vkthing.messages.send(peer_id = peer, message = "@id%s (Оператор) больше не оператор, так как он запретил отправку сообщений в личку от сообщества."%(op), random_id = randid())


















#END
#Code by Oria
