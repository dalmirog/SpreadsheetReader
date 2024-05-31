class Message:
    def __init__(self, createdDate, handle, message, emailAddress):
        self.createdDate = createdDate
        self.handle = handle
        self.message = message
        self.emailAddress = emailAddress
    def to_dict(self):
        return {
            'createdDate': self.createdDate,
            'handle': self.handle,
            'message': self.message,
            'emailAddress': self.emailAddress
        }