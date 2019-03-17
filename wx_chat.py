# 导入模块
from wxpy import *
import re
from get_intent import get_intent
from get_entities import extract_entities
from state_change import send_message
from rasa_nlu.model import Interpreter
from call_API import getValue

# Define the INIT state
INIT=0

# Define the CHOOSE_FUNC state
CHOOSE_FUNC=1

# Define the policy rules
policy = {
    (INIT, "ask_for_information"): (CHOOSE_FUNC, "we can offer you information including real-time price, volume of transaction and the market capitalization of an company, which message do you want to know?"),
    (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you, I am a bot who can provide you with some information about an stock, please ask me about that"),
    (INIT, "has_intent"): (INIT, ""),
    (CHOOSE_FUNC, "has_intent"): (INIT, ""),
    (CHOOSE_FUNC, "none"): (CHOOSE_FUNC, "I'm sorry - I'm not sure how to help you"),
}

intents = {"real_time_price", "volume_of_transactions", "market_capitalization"}

interpreter = Interpreter.load("D:\\python_project\\./projects/default/default\\model_20190316-123239")
print("load ok!")

# 初始化机器人，扫码登陆
bot = Bot()

my_friend = bot.friends().search('扬眉剑出鞘', sex=MALE)[0]

# 发送文本给好友
my_friend.send('Hello we are already providing you our service!')

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

state = INIT
intent = ""
entity = ""
# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    global intent
    global entity
    global state
    pattern = re.compile(r'.*(b|B)ye$')
    if pattern.match(msg.text):
        return
    if intent not in intents:
        intent = get_intent(interpreter, msg.text)
    if len(entity) == 0:
        entity = extract_entities(msg.text)
    state, response = send_message(policy, state, intent)
    if len(response) == 0:
        # call api result
        if len(entity) != 0:
            print(entity, intent)
            my_friend.send(getValue(entity, intent))
            intent = ""
            entity = ""
        else:
            # 判断是否有实体
            my_friend.send("which organization do you want to know?")
        # 重置state
    else:
        my_friend.send(response)
    #return 'received: {} ({})'.format(msg.text, msg.type)

# 进入 Python 命令行、让程序保持运行
embed()