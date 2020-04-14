import os
import time
import random
import platform
youros = platform.system()
if youros == 'Linux':
    ccomm = 'clear'
elif youros == 'Windows':
    ccomm = 'cls'
	
clear = lambda: os.system(ccomm)
clear()
names = [
    'Fluid',
    'Fustie',
    'Mondis',
    'gdLBO',
    'littn3r',
    'keimoger',
    'Wireman',
    'Sava',
    'Anna',
    'Vasya',
    'Petrovich',
    'Lenor',
    'Urbanichka',
    'Kalik'
]
uname = random.choice(names)
print('Antivirus for coronavirus v1.0 started')
print()
def testcorona():
    print("Ваше имя", uname)
    print("Антивирус начал проверку...")
    time.sleep(10)
    coronavirus2 = random.choice([1, 2, 3, 4])
    healrand = random.choice([1, 2])
    if coronavirus2 == 1:
        print("Чист.")
    elif coronavirus2 == 2:
        print("Нужна быстрая мед.помощь ваша стадия -", coronavirus2)
        print("Вы идёте в ближайшую больницу")
        time.sleep(3)
        print("Вы прибыли в место похожее на больницу")
        print("Вахтёр: - ваше имя если я не ошибаюсь", uname)
        print(uname,": - Да это моё имя помогите быстрее.")
        time.sleep(3)
        print("Вас провели в палату и дали пробную вакцину")
        print("Пытаюсь вылечиться...")
        time.sleep(5)
        if healrand < 2:
            print("Вам не удалось вылечиться, вы начинаете сильнее заболевать...")
            time.sleep(5)
            print("У вас болит голова, антивирус начинает само удаление...")
            time.sleep(5)
            print("Заражённый обезврежен")
        else:
            coronavirus2 = 1
            print("Вам удалось вылечиться!")
    elif coronavirus2 == 3:
        print("Я заражён! Чёрт! Ваша стадия -", coronavirus2)
    elif coronavirus2 == 4:
        print("Вы не можете вылечиться ваша стадия - критическая. Начинаю само удаление...")
        time.sleep(5)
        if healrand > 1:
            print("Антивирусу не удалось обезвередить заражённого, вы начали заражать других.")
            time.sleep(5)
            print("В городах начинается коллапс и ваше заражение уже дошло до многих.")
        else:
            print("Само удаление завершено!")
testcorona()
#---Второй запуск---
#time.sleep(10)
#clear()
#print("Тест пройден! Запускаю второй раз...")
#time.sleep(3)
#testcorona()