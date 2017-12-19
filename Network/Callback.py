
class Callback(object):
    def __init__(self, func, action, obj):
        self.function = func
        self.action = action
        self.object = obj
