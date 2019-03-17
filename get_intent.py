
def get_intent(interpreter, message):
    result = interpreter.parse(message)["intent"]
    #print(json.dumps(result, indent=2))
    print(result['name'])
    return result['name']












