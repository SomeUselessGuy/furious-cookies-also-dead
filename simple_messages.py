#Библиотека обработки "простых" сообщений

#ПООООДРУБАЕМ ВКУСНЕЙШИЕ БИБЛИОТЕКИ ОБРАБОТКИ ТЕКСТА, СОХРАНЕНИЯ СООБЩЕНИЙ А ЕЩЕ ПЕЧЕНЕК!
from func import read
from urllib.parse import unquote



global spam
spam = ["", 0] #Предыдущее сообщение + кол-во повторов

gudwords = read("words/good.txt").lower() #Хорошие слова
badwords = read("words/bad.txt").lower() #Плохие слова


def nice(text):
    text = text.lower()
    for s in "*':;/.,([{}])=+-|^%$#@!?&№\"": #Убираем все лишние символы
        text = text.replace(s, "")
    global spam
    if text == spam[0]:
        spam[1] += 1
    else:
        spam = [text, 1]

    gudness = 0 #Сумма
    obsl = 0 #Употребление ненормативной лексики
    grr = 0 #Употребление очень даже нормативной лексики
    row = ["", 0] #Кол-во одинаковых слов подряд
    
    #ААААААААААА перед просмотром след. части убедитесь, что вы не беременный несовершеннолетний ребенок с психическими расстройствами и неприятием мата
    for t in text.split(" "):
        for s in badwords.split("\n"):
            if t == s:
                obsl += 1
        for s in gudwords.split("\n"):
            if t == s:
                grr += 1
                if row[0] == s:
                    row[1] += 1
                    if row[1] > 4:
                        if grr > 0:
                            grr = 0
                        else:
                            grr -= 1.5
                else:
                    row = [s, 1]


    if spam[1] >= 4:
        gudness = -(spam[1] - 3) * 2 - obsl
    elif obsl > grr / 2:
        gudness = 0
    elif obsl > 0:
        gudness = obsl
    elif grr == 0:
        if grr < 8:
            gudness = grr * 2
        else:
            gudness = -0.5
    else:
        gudness = 1



    return {
        "points": gudness
    }