#Главный скрипт
#TODO: заменить мусор на log()

#Импорт сторонних библиотек
import vk, requests, json
#Импорт функций из моих библиотек (приложу их в отдельном файле)
from func import get_token, stop, log, get_randid as randid, getname_init
#Импортируем ядро сообщений
import main_messages as mcore
#Импортируем библиотеку пользователей
import userdata as user

#Получение токена
global token
token = get_token()

#Проверка на токен
if not token:
    stop("Файла token.token не существует!\nВнесите туда access_token группы.")

#Создание сессии вк
vk_session = vk.Session()
vk_api = vk.API(vk_session, access_token = token, v = 5.103)

#Создание сессии... интернета?
eth_session = requests.Session()

#Проверка на валидность токена
try: 
    data = vk_api.groups.getById()[0]   #Получаем информацию о текущем токене.
                                        #Неверный токен - выдаст ошибку
    mcore.initialize(data, vk_api) #Передаем в ядро сообщений данные о боте
    getname_init(vk_api) #ИИИИИИИнициализируем получение имени
    log("Получен доступ от имени %s!"%(data["name"])) #Уведомляем хоста об успешном получении данных
except vk.exceptions.VkAPIError as err: #Если токен не валидный
    if err.is_access_token_incorrect() or err.code == vk.exceptions.AUTHORIZATION_FAILED:
        log("Неверный токен!")
    else:
        log("Неизвестная ошибка!")
    raise
except: #Если что-то еще (нет функции log, mcore не инициализирован, тд)
    log("Неизвестная ошибка!")
    raise
log("Проверка... пройдена?")
#BOTS
longpoll = key = ts = False #Обнуляем данные
while True: #Запускаем бесконечный цикл
    if not longpoll or not key or not ts: #Если один из данных для получения... данных (?) не валиден
        try:
            loc_a = vk_api.groups.getLongPollServer(group_id = data["id"]) #Получаем лонгпулл
        except vk.exceptions.VkAPIError as err:
            if err.code == vk.exceptions.ACCESS_DENIED:
                stop("Нет доступа.\n%s"%(err.message))
            else:
                stop("Неожиданная ошибка!\n%s"%(err.message))
        except:
            stop("Неизвестная ошибка!")
        #Определяем ts, key и ссылку на лонгпулл
        ts = loc_a['ts']
        key = loc_a['key']
        longpoll = loc_a['server']
        print(longpoll)
        log("Got longpoll server!")
    try: #Делаем запрос с таймаутом в шесть и пять секунд (не спрашивайте)
        dd = eth_session.post(longpoll, {"ts": ts,
                                         "act": "a_check",
                                         "key": key,
                                         "wait": 5,
                                         "mode": 2}, timeout = 6)
    except requests.exceptions.ReadTimeout: #Если таймаут
        log("Таймаут получения лонгпула.")
        continue
    except KeyboardInterrupt: #Если ручной выход через CTRL+C
        stop("Ручной выход.")
    except Exception as er: #Если кодер дурак
        log("Неизвестная ошибка.\n -> %s"%(er))
        continue
    if dd.status_code == 200: #Если доступ прошел
        dd = json.loads(dd.text) 
        if "failed" in dd: #Если ошибка
            if dd["failed"] == 1: #ts устарел
                ts = dd["ts"]
            elif dd["failed"] == 2 or dd["failed"] == 3: #key устарел or лонгпул устарел
                key = None
            continue
        ts = dd["ts"] #Обновляем ts
        for upd in dd["updates"]: #Проверяем обновления
            #print(upd)
            if upd["type"] == "message_new" and "object" in upd: #...
                msg = upd["object"]["message"] #Получаем объект сообщения
                answer = mcore.proceed(msg) #Получаем ответы на сообщение из ядра
                for resp in answer: #Проверяем ответы
                    if resp and resp.response: #Если ответ валидный
                        target = resp.target #Проверяем цель
                        if not target: #Чиним цель в случае ее отсутствия
                            target = msg["peer_id"]
                        if resp.action == "send": #Если нужно отправить сообщение
                            vk_api.messages.send(peer_id = target, message = resp.response, random_id = randid())
                        elif resp.action == "remove": #Если нужно удалить участника беседы
                            try:
                                vk_api.messages.removeChatUser(chat_id = target - 2000000000, member_id = resp.response)
                            except vk.exceptions.VkAPIError as err:
                                if err.code == 100:
                                    log("Что-то пошло не так - где-то мы пролюбили передачу беседы")
                                elif err.code == 15:
                                    mcore.operator(target, "У беседы, в которой вы являетесь оператором, включена опция кика людей, но нет админки. Исправьте это недоразумение в настройках либо бота, либо беседы.\nЭто сообщение может возникать также в том случае, если бот пытается кикнуть администратора. Игнорируйте подобные случаи.\nЦель: @id%s"%(resp.response))
                            except: #TODO: исправить это
                                raise

                                















#END
#Code by Oria
