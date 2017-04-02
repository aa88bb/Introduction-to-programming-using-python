class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False
    def __init__(self,a,b,c):
        self.channel = a
        self.volumeLevel = b
        self.on = c

    def turnOn(self):
        self.on = True

    def setChannel(self,channel):
        self.channel = channel


myTV = TV(89,2,False)
# myTV.channel = 8
# myTV.setChannel(888)
print(myTV.channel)