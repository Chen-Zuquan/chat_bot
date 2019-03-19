# 导入模块
from wxpy import *
import re
from get_intent import get_intent
from get_entities import extract_entities
from state_change import send_message
from rasa_nlu.model import Interpreter
from call_API import getValue
from get_time import getTime

# Define the INIT state
INIT=0

# Define the CHOOSE_FUNC state
CHOOSE_FUNC=1

# Define the CHOOSE_ state
CHOOSE_TIME=2

# Define the policy rules
policy = {
    (INIT, "ask_for_information"): (CHOOSE_FUNC, "we can offer you information including real-time price, volume of transaction and the market capitalization of an company, which wolud you like?"),
    (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you, I am a chat_bot who can provide you with some information about an stock, please ask me about that"),
    (INIT, "intent_with_time"): (INIT, ""),
    (INIT, "intent_without_time"): (CHOOSE_TIME, "please tell us the detailed time, just like 2019-01-01"),
    (CHOOSE_FUNC, "intent_without_time"): (CHOOSE_TIME, "please tell us the valid and detailed time, just like 2019-01-01"),
    (CHOOSE_FUNC, "intent_with_time"): (INIT, ""),
    (CHOOSE_FUNC, "none"): (CHOOSE_FUNC, "I'm sorry - I'm not sure how to help you?"),
    (CHOOSE_TIME, "intent_without_time"): (CHOOSE_TIME, "please tell us the valid and detailed time, just like 2019-01-01"),
    (CHOOSE_TIME, "intent_with_time"): (INIT, ""),
}

intents = {"real_time_price", "volume_of_transactions", "market_capitalization"}

with open('projects/model_path', 'r') as f:
    model_directory = f.read()
interpreter = Interpreter.load(model_directory)
print("load ok!")

bot = Bot()
my_friend = bot.friends().search('陈祖泉', sex=MALE)[0]
my_friend.send('Hello we are already providing you our service!')
@bot.register()
def print_others(msg):
    print(msg)

state = INIT
intent = ""
entity = ""
time = ""
# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    global intent
    global entity
    global state
    global time
    pattern = re.compile(r'.*(b|B)ye$')
    if pattern.match(msg.text):
        my_friend.send("I hope I have provided something useful!")
    if intent not in intents:
        intent = get_intent(interpreter, msg.text)
    if len(entity) == 0:
        entity = extract_entities(msg.text)
    if len(time) == 0:
        time = getTime(msg.text)
    state, response = send_message(policy, state, intent, time)
    if len(response) == 0:
        # call api result
        if len(entity) != 0:
            print(entity, intent, time)
            my_friend.send(getValue(entity, intent, time))
            intent = ""
            entity = ""
            time = ""
        else:
            # 判断是否有实体
            my_friend.send("which organization do you want to know?")
        # 重置state
    else:
        my_friend.send(response)
    #return 'received: {} ({})'.format(msg.text, msg.type)

# 进入 Python 命令行、让程序保持运行
embed()