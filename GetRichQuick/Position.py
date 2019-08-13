class Position:
    def __init__(self, stock, volume):
        self.stock = stock
        self.volume = volume

    def updatePosition(self, volume):
        if self.volume + volume < 0:
            print('Negative position not allowed')
        else:
            self.volume += volume
