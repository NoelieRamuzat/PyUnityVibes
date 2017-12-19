
class Color(object):

    def __init__(self, red, green, blue, alpha):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def toString(self):
        return "({}, {}, {}, {})".format(self.red, self.green, self.blue, self.alpha)