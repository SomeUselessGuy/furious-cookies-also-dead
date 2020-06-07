#Библиотека обработки "простых" сообщений
global spam
spam = ["", 0] #Предыдущее сообщение + кол-во повторов



def nice(text):
    global spam
    if text == spam[0]:
        spam[1] += 1
    else:
        spam = [text, 1]

    gudness = 0
    
    if spam[1] >= 4:
        gudness = -(spam[1] - 3) * 2
    else:
        gudness = 1


    return {
        "points": gudness
    }