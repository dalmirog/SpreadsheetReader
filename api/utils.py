from api.message import Message

# def create_messages_from_raw_values(rawValues):
#     messages = []
#     for rv in rawValues:
#         if len(rv) >= 4 and all(rv[:4]):
#             messages.append(Message(rv[0], rv[1], rv[2], rv[3]))
#     return messages

def create_messages_from_raw_values(rawValues):
    # Extract the property names from the first sublist
    property_names = rawValues[0]

    # Initialize an empty list to hold the dictionaries
    list_of_dicts = []

    # Iterate over the subsequent sublists
    for values in rawValues[1:]:
        # Create a dictionary by pairing property names with values
        record = {property_names[i]: (values[i] if i < len(values) and values[i] != '' else None) for i in range(len(property_names))}
        # Add the dictionary to the list
        list_of_dicts.append(record)
        # Todo: sort by date and group by email

    return list_of_dicts