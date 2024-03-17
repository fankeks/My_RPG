import cv2


class StoneWall:
    def __init__(self, path='C://Users//Hp//Desktop//PyCharm//My_RPG//Textures//Stone_Wall//1.jpg'):
        self.__picture = cv2.imread(path, 1)


    @property
    def picture(self):
        return self.__picture