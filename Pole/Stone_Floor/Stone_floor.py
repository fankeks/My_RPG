import cv2


class StoneFloor:
    def __init__(self, path='C://Users//Hp//Desktop//PyCharm//My_RPG//Textures//Stone_Floor//1.jpg'):
        self.__picture = cv2.imread(path, 1)


    @property
    def picture(self):
        return self.__picture