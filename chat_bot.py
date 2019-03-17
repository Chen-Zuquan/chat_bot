import re
from get_intent import get_intent
from get_entities import extract_entities
from state_change import send_message
from rasa_nlu.model import Interpreter

# Define the INIT state
INIT=0

# Define the CHOOSE_FUNC state
CHOOSE_FUNC=1



# Define the policy rules
policy = {
    (INIT, "ask_for_information"): (CHOOSE_FUNC, "we can offer you information including real-time price, volume of transaction and the market capitalization of an company, which wolud you like?"),
    (INIT, "none"): (INIT, "I'm sorry - I'm not sure how to help you, I am a chat_bot who can provide you with some information about an stock, please ask me about that"),
    (INIT, "has_intent"): (INIT, ""),
    (CHOOSE_FUNC, "has_intent"): (INIT, ""),
    (CHOOSE_FUNC, "none"): (CHOOSE_FUNC, "I'm sorry - I'm not sure how to help you?"),
}

intents = {"real_time_price", "volume_of_transactions", "market_capitalization"}
if __name__ == '__main__':
    interpreter = Interpreter.load("D:\\python_project\\./projects/default/default\\model_20190316-123239")
    print("we are already to provide service with you!")
    state = INIT
    intent = ""
    entity = ""
    while True:
        message = input()
        pattern = re.compile(r'.*(b|B)ye$')
        if pattern.match(message):
            break
        if intent not in intents:
            intent = get_intent(interpreter, message)
        if len(entity) == 0:
            entity = extract_entities(message)
        state, response = send_message(policy, state, intent)
        if len(response) == 0:
            #call api result
            if len(entity) != 0:
                print("call API")
            else:
                #判断是否有实体
                while True:
                    print("which organization do you want to know?")
                    mes = input()
                    ent = extract_entities(mes)
                    if len(ent) != 0:
                        break
                print("call API")
            intent = ""
            entity = ""
            #重置state
        else:
            print(response)

