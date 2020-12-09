class Track:
    def __init__(self, top, left, color, img, length, rot, perX, perY, occupied, edge):
        self.top = top
        self.left = left
        self.color = color
        self.img = img
        self.rot = rot
        self.length = length
        self.perX = perX
        self.perY = perY
        self.occupied = occupied
        self.edgeData = edge

    def getEdgeData(self):
        return self.edgeData

    def setTop(self, top):
        self.top = top

    def getTop(self):
        return self.top

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setHeight(self, height):
        self.height = height

    def getHight(self):
        return self.height

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getImg(self):
        return self.img

    def getRot(self):
        return self.rot

    def getLength(self):
        return self.length

    def getPerX(self):
        return self.perX

    def getPerY(self):
        return self.perY

    def getOccupied(self):
        return self.occupied

    def setOccupied(self, occupied):
        self.occupied = occupied
