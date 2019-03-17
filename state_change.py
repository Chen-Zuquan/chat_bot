
def send_message(policy, state, intent, time):
    #print("USER : {}".format(message))
    #print(state, intent)
    new_state, response = respond(policy, state, intent, time)
    #print("BOT : {}".format(response))
    return new_state, response

def respond(policy, state, intent, time):
    (new_state, response) = policy[(state, interpret(intent, time))]
    return new_state, response

intents = {"real_time_price", "market_capitalization"}
def interpret(intent, time):
    if intent == "ask_for_information":
        return intent
    if intent in intents:
        return "intent_with_time"
    if intent != "volume_of_transactions":
        return 'none'
    if len(time) == 0:
        return "intent_without_time"
    else:
        return "intent_with_time"


