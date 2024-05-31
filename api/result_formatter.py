from datetime import datetime
from collections import defaultdict

def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%m/%d/%Y %H:%M:%S"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date format for '{date_str}' is not supported")

def sort_messages_by_date_desc(messages):
    return sorted(messages, key=lambda msg: parse_date(msg.createdDate), reverse=True)


def filter_messages(messages, max_per_email=5):
    email_count = defaultdict(int)
    filtered_messages = []

    for message in messages:
        if email_count[message.emailAddress] < max_per_email:
            filtered_messages.append(message)
            email_count[message.emailAddress] += 1
    
    return filtered_messages

def single_line(messages):
    filtered_messages = filter_messages(messages)
    sorted_messages = sort_messages_by_date_desc(filtered_messages)
    formatted_messages = [f"[{msg.handle}] {msg.message}" if msg.handle else msg.message for msg in sorted_messages]
    return ' - '.join(formatted_messages)

def to_dict(messages):
    filtered_messages = filter_messages(messages)
    sorted_messages = sort_messages_by_date_desc(filtered_messages)
    return [message.to_dict() for message in sorted_messages]