from api.message import Message

def create_messages_from_raw_values(rawValues):
    messages = []
    for rv in rawValues:
        if len(rv) >= 4 and all(rv[:4]):
            messages.append(Message(rv[0], rv[1], rv[2], rv[3]))
    return messages
