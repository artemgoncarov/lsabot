import time
import sys
from vkbottle.bot import Bot, Message
import random
import asyncio
import aiosqlite
from vkbottle import BaseStateGroup
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import random
import os
import time
from vkbottle import API

token = "93ffbc4048b9d780354f6003146b650a6a988944b0deabda03ed8b7585105f11a1f28b91cd5fb33b552b2"

bot = Bot(token=token)

infa = [[534563953, "Cambino_Timov", "Сержант [4]", "0"],
        [596611142, "Daniil_Its", "Генерал [10]", "0"]
        # [580832274, "Arseny_Hiro", "Безработный [0]", "0"]
        ]

moderators = [
    534563953,
    596611142
]

uid: int = 0

@bot.on.message(text="/letsplay")
async def letsplay(message: Message):
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)
    await message.answer("⚠ | Уведомление! @all Руководство фракции вызывает Вас в игру.")
    time.sleep(3600)



@bot.on.message(text="/qq")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))


@bot.on.message(text="/whoi")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    a = random.randint(0,5)
    name = None
    if a == 0:
        name = "жареная картошка"
    if a == 1:
        name = "соленый помидор"
    if a == 2:
        name = "вяленая петрушка"
    if a == 3:
        name = "недоделанный овощ"
    if a == 4:
        name = "вкусный пельмень"
    if a == 5:
        name = "бургер из кфс"
    await message.answer("Привет, @id{}".format(users_info[0].id) + " (" + users_info[0].first_name + " " + users_info[0].last_name + ")" + ", ты " + name)

@bot.on.message(text="/hello")
async def help(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, @id{}".format(users_info[0].id) + "(" + "{}".format(users_info[0].first_name) + " {}".format(users_info[0].last_name) +")")



@bot.on.message(text="/nicks")
async def nicks(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    l = len(infa) + 1
    for i in range(0, l):
        await message.answer("@id{}".format(infa[i][0]) + " ("  + infa[i][1] + ")" )


@bot.on.message(text="/myinfo")
async def information(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    id_user = users_info[0].id
    l = len(infa)
    lst = []
    for i in range(0, l):
        lst.append(infa[i][0])
    if id_user in lst:
        i = lst.index(id_user)
        await message.answer("👤 | Ваш профиль фракции ЛСа:" + "\n✨ | Никнейм: " + infa[i][1] + "\n🎃 | Ранг: " + infa[i][2] + "\n💎 | Баллы: " + infa[i][3])
    else:
        await message.answer("❗Ошибка, вы не зарегистрированы❗")




@bot.on.message(text="/help")
async def help(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Список доступных команд: \n /help \n /myinfo \n /hello \n /qq \n /regme <nick> \n /whoi \n /changenick <nick>")


@bot.on.message(text="/regme <nick>")
async def testid(message: Message, nick=None):
    users_info = await bot.api.users.get(message.from_id)
    uid = users_info[0].id
    lst = []
    l = len(infa)
    for i in range(0, l):
        lst.append(infa[i][0])
    if uid not in lst:
        infa.append([uid,nick, "Безработный[0]", "0"])
        await message.answer("💎 Участник успешно зарегистрирован! 💎")
    else:
        await message.answer("❗Ошибка, вы уже зарегистрированы❗")

@bot.on.message(text="/changenick <nick>")
async def changenick(message: Message, nick=None):
    users_info = await bot.api.users.get(message.from_id)
    uid = users_info[0].id
    lst = []
    l = len(infa)
    for i in range(0, l):
        lst.append(infa[i][0])
    if uid in lst:
        i = lst.index(uid)
        infa[i][1] = nick
    else:
        await message.answer("❗Ошибка, вы не зарегистрированы❗")

@bot.on.message(text="/info <id>")
async def find(message: Message, id=None):
    users_info = await bot.api.users.get(message.from_id)
    aid = users_info[0].id
    uid = id
    uid = id.split("|")
    uid = uid[0].split("[")
    uid = uid[1].split("id")
    uid = int(uid[1])
    lst = []
    l = len(infa)
    for i in range(0, l):
        lst.append(infa[i][0])
    if aid in moderators:
        i = lst.index(uid)
        await message.answer("👤 | Профиль игрока фракции ЛСа:" + "\n✨ | Никнейм: " + infa[i][1] + "\n🎃 | Ранг: " + infa[i][2] + "\n💎 | Баллы: " + infa[i][3])
    else:
        await message.answer("❗Ошибка, недостаточно прав❗")

@bot.on.message(text="/makemod <id>")
async def makemod(message: Message, id=None):
    users_info = await bot.api.users.get(message.from_id)
    aid = users_info[0].id
    uid = id
    uid = id.split("|")
    uid = uid[0].split("[")
    uid = uid[1].split("id")
    uid = int(uid[1])
    if aid in moderators:
        moderators.append(uid)
        await message.answer("💎 Участник успешно назначен модератором! 💎")
    else:
        await message.answer("❗Ошибка, недостаточно прав❗")

@bot.on.message(text="/unmakemod <id>")
async def unmakemod(message: Message, id=None):
    users_info = await bot.api.users.get(message.from_id)
    aid = users_info[0].id
    uid = id
    uid = id.split("|")
    uid = uid[0].split("[")
    uid = uid[1].split("id")
    uid = int(uid[1])
    if aid in moderators:
        moderators.remove(uid)
    else:
        await message.answer("❗Ошибка, недостаточно прав❗")

@bot.on.message(text="/setballs <id> <balls>")
async def setballs(message: Message, id=None, balls=None):
    users_info = await bot.api.users.get(message.from_id)
    aid = users_info[0].id
    uid = id
    uid = id.split("|")
    uid = uid[0].split("[")
    uid = uid[1].split("id")
    uid = int(uid[1])
    lst = []
    l = len(infa)
    for i in range(0, l):
        lst.append(infa[i][0])
    if aid in moderators:
        i = lst.index(uid)
        infa[i][3] = balls
        await message.answer("💎 Количество баллов успешно измененено! 💎")
    else:
        await message.answer("❗Ошибка, недостаточно прав❗")

@bot.on.message(text="/setrank <id> <rank>")
async def setrank(message: Message, id=None, rank=None):
    rang = None
    if rank == "0":
        rang = "Безработный [0]"
    if rank == "1":
        rang = "Рядовой [1]"
    if rank == "2":
        rang = "Капрал [2]"
    if rank == "3":
        rang = "Старшина [3]"
    if rank == "4":
        rang = "Сержант [4]"
    if rank == "5":
        rang = "Лейтенант [5]"
    if rank == "6":
        rang = "Капитан [6]"
    if rank == "7":
        rang = "Майор [7]"
    if rank == "8":
        rang = "Подполковник [8]"
    if rank == "9":
        rang = "Полковник [9]"
    if rank == "10":
        rang = "Генерал [10]"
    if rank == "11":
        rang = "Министр Обороны [11]"
    if rank == "12":
        rang = "Администратор"
    users_info = await bot.api.users.get(message.from_id)
    aid = users_info[0].id
    uid = id
    uid = id.split("|")
    uid = uid[0].split("[")
    uid = uid[1].split("id")
    uid = int(uid[1])
    if aid in moderators:
        for i in range(0, len(infa)):
            if uid in infa[i]:
                infa[i][2] = rang
                await message.answer("💎 Ранг пользователя успешно установлен! 💎")
    else:
        await message.answer("❗Ошибка, недостаточно прав❗")





bot.run_forever()

