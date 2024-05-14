class Message:
    def __init__(self, createdDate, handle, message):
        self.createdDate = createdDate
        self.handle = handle
        self.message = message
    def to_dict(self):
        return {
            'createdDate': self.createdDate,
            'handle': self.handle,
            'message': self.message
        }