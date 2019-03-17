
def send_message(policy, state, intent):
    #print("USER : {}".format(message))
    #print(state, intent)
    new_state, response = respond(policy, state, intent)
    #print("BOT : {}".format(response))
    return new_state, response

def respond(policy, state, intent):
    (new_state, response) = policy[(state, interpret(intent))]
    return new_state, response

intents = {"real_time_price", "volume_of_transactions", "market_capitalization"}
def interpret(intent):
    if intent == "ask_for_information":
        return intent
    if intent not in intents:
        return 'none'
    return 'has_intent'

