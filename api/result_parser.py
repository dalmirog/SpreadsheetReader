from api import message

def ParseResult(values):
    results = []
    for value in values:
        results.append(message.Message(value[0],value[1],value[2]))
    return values