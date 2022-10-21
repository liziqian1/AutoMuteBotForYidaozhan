import datetime
import logging
import random
import threading
import time
from aiogram import Bot, Dispatcher, executor, types

from config import BOT_TOKEN, WORDS

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
weight: int = 0

YIDAOZHAN_USER_ID = 1778185820
CHITANG_CHAT_ID = -1001193721792

#REPLY_MESSAGE = ('你说的对，但是我认为你应该在 iPhone 14 Pro Max 非海南免税版上运行 MSDOS 然后执行 sudo pacman -Syu ，然后他就可以把 NixOS 升级到最新版本，这就意味着一个风滚草用户开始了桶滚，不过 AMD 显卡的用户要注意，Windows Update 可能会搞坏你在 Android 上的 Nvidia 显卡驱动，所以更新 Windows 10 Mobile 可以给 iPhone 3gs 用户带来更佳的 Gentoo 使用体验，综上所述，用 波音787 搞渗透是可行的，但是前提是你能够熟练的开火车，这样才能用胶带开启虫洞进行星际穿越。', '你说得对，但是 Python 是由井盖人 Guido van Rossum 自主研发的一款全新编程语言。在一个被称作脚本语言的幻想世界里，被选中的人将被授予 AttributeError: NoneType，导引空指针之力。你将扮演一位名叫 PyCharm 的神秘角色，在自由的旅行中拯救 SyntaxError、MemoryError，和他们一起击败 OSError，找回失散的 Exception——同时，逐步发掘 Cpython 的真相。', '我觉得吃披萨应该加95号汽油，并且应该加到试管底部1/3的位置，这样是为了拉格朗日点能够在爱因斯坦质能方程中找到属于自己的北回归线，如果不小心加错加了92号汽油，那就不好办了，首先要找到老爹让他念出戊戌变法，防止发动机和神经中枢对撞产生等离子火花和伽马射线，按照孔子的说法，我们还要把进化论里的化学方程式配平，这样才能让海尔兄弟放过舒克和贝塔', '不敢苟同，我认为炒意大利面应该拌老干妈，因为螺丝钉向内扭的时候会产生二氧化碳，不利于经济发展，并且野生的乌鸦也会捕食三角函数。所以不论承重墙能不能打赢DK，宋江也能赢得世界杯', '我不敢苟同这样的说法，首先我认为老坛酸菜应该拥有准考证号，这样更能证明水是剧毒，但李白和白垩纪大灭绝的关系是属于乘法口诀表里的广义相对论，因此我推算出牛肉和原子弹的味道一样，喜欢吃肉和1+1=2这两种观点有很大的冲突，有人会觉得这观点偏激了，我们可以得知牛顿被苹果砸中后发现了钢筋混凝土喜欢鲨鱼后让莫比乌斯环分成两面，我们也可以得出西伯利亚与三体视频聊天通话中谈到的是米老鼠是应该按F，还是加鱼子酱的话题，总体来说，这都不影响潘子与虎哥在一起商讨鲨鱼应该吃混凝土还是穿内裤的问题', '我认为好的意大利粥的做法应该是五常大米加一点长白山上的特仑苏搅拌成薄薄的厚片，因为这样可以生成美拉德反应，并且有利于经济的飞速发展，从而得出永乐大典失传的真相，爱因斯坦福说过，好的阿尔法突袭可以在一瞬间斩杀程咬金，防止他开大，再向B区扔个闪光蛋，这样才能在明朝小冰河时期拯救更多的黑猫警长。')

async def ban_user(message: types.Message):
    weight = 0
    await message.reply('为了您的身心健康，我决定让您休息10分钟。\n~~如有误判，那就有吧。~~')
    permissions = types.ChatPermissions(can_send_messages=False, can_send_media_messages=False)
    await bot.restrict_chat_member(chat_id=CHITANG_CHAT_ID, user_id=YIDAOZHAN_USER_ID, permissions=permissions,
                                   until_date=datetime.datetime.now() + datetime.timedelta(minutes=10))


async def ban_user_(message: types.Message):
    weight = 0
    await message.reply('请您休息10分钟。')
    permissions = types.ChatPermissions(can_send_messages=False, can_send_media_messages=False)
    await bot.restrict_chat_member(chat_id=CHITANG_CHAT_ID, user_id=YIDAOZHAN_USER_ID, permissions=permissions,
                                   until_date=datetime.datetime.now() + datetime.timedelta(minutes=10))

@dp.message_handler()
async def message_handler(message: types.Message):
    if message.from_user.id != YIDAOZHAN_USER_ID:
        return
    
    lower_message = message.text.lower()

    for add_weight in WORDS:
        for word in WORDS[add_weight]:
            if word in lower_message:
                weight += add_weight
    
    if '我' in lower_message and ('想' in lower_message or '要' in lower_message or '得' in lower_message) and ('冷静' in lower_message or '禁言' in lower_message):
        await ban_user(message)
    
    print(f'{lower_message} {weight}')

    if weight >= 100:
        print(lower_message)
        await ban_user(message)

@dp.message_handler(commands=['mute'])
async def send_welcome(message: types.Message):
    if message.from_user.id != YIDAOZHAN_USER_ID:
        return
    await ban_user_(message)

def create_timer():
    t = threading.Timer(300, clear_weight)
    t.start()

def clear_weight():
    create_timer()
    weight = 0

if __name__ == '__main__':
    create_timer()
    executor.start_polling(dp, skip_updates=False)